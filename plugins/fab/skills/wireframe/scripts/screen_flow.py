#!/usr/bin/env python3
"""Bounded Canvas presentation edits; no product model or layout inference.

Explicit node kinds select colors. Explicit edge kinds move existing labels to
documentary frames. The audit can collapse those frames back to original edges.
Never overwrites the input or an existing output. Standard library only.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import textwrap
from pathlib import Path

PALETTE = {'module': '6', 'modal': '#0062ff', 'empty': '#b8b8b8',
           'action': '5', 'error': '1', 'event': '3',
           'screen': None, 'result': None, 'condition': None,
           'navigation': None, 'index': None, 'legend': None}


def indexed(items):
    result = {}
    for item in items:
        key = item.get('id')
        if not isinstance(key, str) or not key or key in result:
            raise ValueError('Missing/duplicate ID')
        result[key] = item
    return result


def overlap(a, b, gap=0):
    return (max(a['x'], b['x']) < min(a['x'] + a['width'], b['x'] + b['width']) + gap
            and max(a['y'], b['y']) < min(a['y'] + a['height'], b['y'] + b['height']) + gap)


def estimated_height(text, width):
    """Conservative fallback estimate, never native Markdown-fit proof."""
    columns = max(8, int((width - 32) / 13))
    rows = sum(max(1, len(textwrap.wrap(line, columns))) for line in text.splitlines())
    return max(64, 32 + rows * 25)


def project(original, node_kinds=None, edge_kinds=None, placements=None):
    node_kinds, edge_kinds, placements = node_kinds or {}, edge_kinds or {}, placements or {}
    if any(not isinstance(mapping, dict) for mapping in (node_kinds, edge_kinds, placements)):
        raise ValueError('Explicit edits must be mappings')
    canvas = copy.deepcopy(original)
    nodes = indexed(canvas['nodes']); edges = indexed(canvas['edges'])
    for edge in edges.values():
        if edge['fromNode'] not in nodes or edge['toNode'] not in nodes:
            raise ValueError('Dangling edge')
    if set(placements) - set(edge_kinds):
        raise ValueError('Placement outside selected edge scope')
    audit = {'schemaVersion': 1, 'nodeColors': {}, 'frames': []}
    for key, kind in node_kinds.items():
        if key not in nodes or kind not in PALETTE:
            raise ValueError('Unknown node or explicit kind')
        node = nodes[key]
        audit['nodeColors'][key] = {'present': 'color' in node, 'value': node.get('color'), 'kind': kind}
        if PALETTE[kind] is None:
            node.pop('color', None)
        else:
            node['color'] = PALETTE[kind]
    replacements = {}
    for key, kind in edge_kinds.items():
        if key not in edges or kind not in ('action', 'condition', 'result'):
            raise ValueError('Unknown edge or explicit frame kind')
        edge = edges[key]; label = edge.get('label')
        if not isinstance(label, str) or not label.strip():
            raise ValueError('Frame requires an existing meaningful label')
        frame_id, first_id, second_id = 'SF-frame-' + key, 'SF-in-' + key, 'SF-out-' + key
        if frame_id in nodes or first_id in edges or second_id in edges:
            raise ValueError('Projection ID collision')
        a, b = nodes[edge['fromNode']], nodes[edge['toNode']]
        geometry = dict(placements.get(key, {}))
        if set(geometry) - {'x', 'y', 'width', 'height'}:
            raise ValueError('Placement contains a non-geometry field')
        if any(type(v) not in (int, float) or not math.isfinite(v) for v in geometry.values()):
            raise ValueError('Non-finite geometry')
        width = geometry.get('width', 220)
        if width <= 32:
            raise ValueError('Frame width too small')
        frame = {'id': frame_id, 'type': 'text', 'text': label,
                 'width': width, 'height': geometry.get('height', estimated_height(label, width))}
        frame['x'] = geometry.get('x', (a['x'] + a['width'] + b['x'] - width) / 2)
        frame['y'] = geometry.get('y', (a['y'] + a['height']/2 + b['y'] + b['height']/2 - frame['height']) / 2)
        if any(not isinstance(frame[k], (int, float)) or not math.isfinite(frame[k]) for k in ('x', 'y', 'width', 'height')):
            raise ValueError('Non-finite geometry')
        if frame['width'] <= 32 or frame['height'] < estimated_height(label, frame['width']):
            raise ValueError('Frame too small for estimated text; native fit still needs inspection')
        if any(overlap(frame, n, 24) for n in nodes.values() if n.get('type') != 'group'):
            raise ValueError('Insufficient clear space; supply a bounded placement, do not move unrelated cards')
        if kind == 'action':
            frame['color'] = PALETTE['action']
        first = {'id': first_id, 'fromNode': edge['fromNode'], 'toNode': frame_id,
                 'fromSide': edge.get('fromSide', 'right'), 'toSide': 'left', 'toEnd': 'arrow'}
        if 'fromEnd' in edge:
            first['fromEnd'] = edge['fromEnd']
        second = {'id': second_id, 'fromNode': frame_id, 'toNode': edge['toNode'],
                  'fromSide': 'right', 'toSide': edge.get('toSide', 'left'), 'toEnd': edge.get('toEnd', 'arrow')}
        if 'color' in edge:
            first['color'] = second['color'] = edge['color']
        nodes[frame_id] = frame; canvas['nodes'].append(frame)
        replacements[key] = [first, second]
        audit['frames'].append({'originalEdge': copy.deepcopy(edge), 'frame': copy.deepcopy(frame),
                                'kind': kind, 'legs': copy.deepcopy([first, second])})
    canvas['edges'] = [leg for edge in canvas['edges'] for leg in replacements.get(edge['id'], [edge])]
    assert_preserved(original, canvas, audit)
    return canvas, audit


def assert_preserved(original, projected, audit):
    """Independent collapse check: exact original fields, order and branches."""
    recovered = copy.deepcopy(projected)
    nodes, edges = indexed(recovered['nodes']), indexed(recovered['edges'])
    frame_ids, first_legs, second_legs = set(), {}, set()
    for record in audit['frames']:
        frame = record['frame']; legs = record['legs']; edge = record['originalEdge']
        if nodes.get(frame['id']) != frame or any(edges.get(e['id']) != e for e in legs):
            raise ValueError('Changed documentary frame or legs')
        if frame['text'] != edge['label'] or (legs[0]['fromNode'], legs[1]['toNode']) != (edge['fromNode'], edge['toNode']):
            raise ValueError('Lost source relation meaning/endpoints')
        frame_ids.add(frame['id']); first_legs[legs[0]['id']] = edge; second_legs.add(legs[1]['id'])
    recovered['nodes'] = [n for n in recovered['nodes'] if n['id'] not in frame_ids]
    for node in recovered['nodes']:
        old = audit['nodeColors'].get(node['id'])
        if old:
            if node.get('color') != PALETTE[old['kind']]:
                raise ValueError('Changed semantic palette')
            if old['present']:
                node['color'] = old['value']
            else:
                node.pop('color', None)
    recovered['edges'] = [first_legs.get(e['id'], e) for e in recovered['edges'] if e['id'] not in second_legs]
    if recovered != original:
        raise ValueError('Source fields, ordering, owners, branches or unrelated content changed')


def write_projection(source, output, spec):
    if not isinstance(spec, dict) or set(spec) - {'sourceSha256', 'nodeKinds', 'edgeKinds', 'placements'}:
        raise ValueError('Unknown edit-spec fields')
    data = source.read_bytes()
    if hashlib.sha256(data).hexdigest() != spec.get('sourceSha256'):
        raise ValueError('Source changed; review current creator edits first')
    audit_path = output.with_suffix(output.suffix + '.projection.json')
    if output.exists() or output.is_symlink() or audit_path.exists() or audit_path.is_symlink():
        raise ValueError('Refuse to overwrite input, output or audit')
    original = json.loads(data)
    canvas, audit = project(original, spec.get('nodeKinds'), spec.get('edgeKinds'), spec.get('placements'))
    audit['sourceSha256'] = spec['sourceSha256']
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8') as f:
        f.write(json.dumps(canvas, ensure_ascii=False, indent=2) + '\n')
    with audit_path.open('x', encoding='utf-8') as f:
        f.write(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
    return canvas, audit


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path); p.add_argument('output', type=Path)
    p.add_argument('--spec', type=Path, required=True)
    args = p.parse_args()
    try:
        canvas, audit = write_projection(args.source, args.output, json.loads(args.spec.read_text()))
    except (ValueError, KeyError) as exc:
        p.exit(1, 'ERROR: ' + str(exc) + '\n')
    print(json.dumps({'output': str(args.output), 'frames': len(audit['frames']),
                      'nodes': len(canvas['nodes']), 'scope': 'static reversible projection; native fit unknown'}))


if __name__ == '__main__':
    main()
