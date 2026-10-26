#!/usr/bin/env python3
"""Explicit Canvas authoring and bounded presentation edits; no product inference.

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
import re
import textwrap
from pathlib import Path

PALETTE = {'module': '6', 'modal': '#0062ff', 'empty': '#b8b8b8',
           'action': '5', 'error': '1', 'event': '3',
           'screen': None, 'result': None, 'condition': '3',
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


def project(original, node_kinds=None, edge_kinds=None, placements=None, composition=None):
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
        if kind in ('action', 'condition'):
            frame['color'] = PALETTE[kind]
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
    if composition is not None:
        compose(canvas, audit, composition)
    assert_preserved(original, canvas, audit)
    return canvas, audit


def vault_map(value):
    """A vault-relative Canvas file, never an inferred native node deep link."""
    if (not isinstance(value, str) or not value.endswith('.canvas')
            or value.startswith(('/', '~')) or any(c in value for c in '[]|#\\\n\r')
            or any(p in ('', '.', '..') for p in value.split('/'))):
        raise ValueError('Expected a vault-relative Canvas path')
    return value


def mark_current_navigation(markdown, current_map):
    """Render the exact current map as emphasis, keeping other destinations linked."""
    current_map = vault_map(current_map)
    return re.sub(r'(?<!!)\[\[([^\]|\n]+)(?:\|([^\]\n]+))?\]\]',
                  lambda m: '**' + (m[2] or Path(m[1]).stem) + '**' if m[1] == current_map else m[0],
                  markdown)


def line(value):
    if not isinstance(value, str) or not value.strip() or any(c in value for c in '\n\r[]|'):
        raise ValueError('Expected a nonempty single-line label')
    return value


def card_text(title, body='', caption=None):
    """Human-facing heading, optional type caption, unambiguous thematic break."""
    title = line(title)
    if not isinstance(body, str):
        raise ValueError('Card body must be text')
    text = '## ' + title
    if caption is not None:
        text += '\n\n' + line(caption)
    if body:
        text += '\n\n---\n\n' + body
    return text


def continuation_text(title, target_map, target_id, target_title, retained, target_label='Target ID',
                      target_display_id=None, caption=None):
    """A named map/surface destination; no inferred caller or native-node jump."""
    if not isinstance(retained, list) or not retained:
        raise ValueError('Continuation needs actual retained context')
    if target_display_id is not None:
        alias = display_id(target_display_id) + ' · ' + line(target_title)
        locator = ''
    else:
        alias = line(target_title)
        locator = '\n\n' + line(target_label) + ': ' + line(target_id)
    body = ('[[' + vault_map(target_map) + '|' + alias + ']]' + locator
            + '\n\n' + '\n'.join('- ' + line(x) for x in retained))
    return card_text(title, body, caption)


def document_node(nodes, key, text, geometry, kind):
    if key in nodes or not isinstance(key, str) or not key:
        raise ValueError('Documentary node ID collision')
    if not isinstance(geometry, dict) or set(geometry) != {'x', 'y', 'width', 'height'}:
        raise ValueError('Explicit documentary geometry required')
    if any(type(v) not in (int, float) or not math.isfinite(v) for v in geometry.values()):
        raise ValueError('Invalid documentary geometry')
    # Estimate visible aliases rather than the hidden vault path length.
    visible = re.sub(r'!?\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', lambda m: m[2] or m[1], text)
    if geometry['width'] <= 32 or geometry['height'] < estimated_height(visible, geometry['width']):
        raise ValueError('Documentary node too small; inspect native fit separately')
    node = dict(id=key, type='text', text=text, **geometry)
    node['fabPresentation'] = kind
    if any(overlap(node, n, 24) for n in nodes.values() if n.get('type') != 'group'):
        raise ValueError('Documentary node overlaps existing content')
    nodes[key] = node
    return node


def compose(canvas, audit, spec):
    """Explicit local orientation and reversible return references, no behavior inference."""
    if not isinstance(spec, dict) or set(spec) - {'mapPath', 'returnReferences', 'panels', 'labels'}:
        raise ValueError('Unknown composition fields')
    current_map = vault_map(spec['mapPath'])
    labels = {'return': 'Return reference', 'target': 'Target ID',
              'source': 'Source transition', 'retained': 'Retained context'}
    custom_labels = spec.get('labels', {})
    if not isinstance(custom_labels, dict) or set(custom_labels) - set(labels):
        raise ValueError('Unknown composition labels')
    labels.update({key: line(value) for key, value in custom_labels.items()})
    returns, panels = spec.get('returnReferences', {}), spec.get('panels', [])
    if not isinstance(returns, dict) or not isinstance(panels, list):
        raise ValueError('Invalid composition collections')
    nodes, edges = indexed(canvas['nodes']), indexed(canvas['edges'])
    audit['returns'], audit['panels'] = [], []
    replacements = {}
    for key, rule in returns.items():
        if key not in edges or not isinstance(rule, dict) or set(rule) != {'label', 'retained', 'reason', 'placement'}:
            raise ValueError('Explicit existing return relation and contract required')
        edge = edges[key]
        if any(key == f['originalEdge']['id'] for f in audit['frames']):
            raise ValueError('An edge cannot be both a frame and a return reference')
        label, reason = line(rule['label']), line(rule['reason'])
        retained = rule['retained']
        if not isinstance(retained, list) or not retained:
            raise ValueError('Return reference needs explicit retained context')
        retained = [line(x) for x in retained]
        target = nodes[edge['toNode']]
        title = target.get('text', target['id']).splitlines()[0].lstrip('# ').strip() or target['id']
        text = ('## ' + label + '\n\n' + labels['return'] + '\n\n---\n\n'
                + '[[' + current_map + '|' + title.replace('|', ' ').replace('[', '').replace(']', '') + ']]'
                + '\n' + labels['target'] + ': ' + target['id'] + '\n\n'
                + (labels['source'] + ': ' + str(edge['label']) + '\n\n' if edge.get('label') else '')
                + labels['retained'] + ':\n' + '\n'.join('- ' + x for x in retained))
        frame = document_node(nodes, 'SF-return-' + key, text, rule['placement'], 'return-reference')
        leg = {'id': key, 'fromNode': edge['fromNode'], 'toNode': frame['id'],
               'fromSide': 'right', 'toSide': 'left', 'toEnd': 'arrow'}
        replacements[key] = leg
        canvas['nodes'].append(frame)
        audit['returns'].append({'originalEdge': copy.deepcopy(edge), 'frame': copy.deepcopy(frame),
                                 'leg': copy.deepcopy(leg), 'targetMap': current_map,
                                 'targetId': target['id'], 'retained': retained, 'reason': reason})
    canvas['edges'] = [replacements.get(e['id'], e) for e in canvas['edges']]
    for panel in panels:
        if not isinstance(panel, dict) or panel.get('kind') not in ('navigation', 'legend'):
            raise ValueError('Unknown orientation panel')
        kind = panel['kind']
        expected = {'id', 'kind', 'title', 'placement', 'groups' if kind == 'navigation' else 'body'}
        if set(panel) != expected:
            raise ValueError('Unknown orientation panel fields')
        text = '## ' + line(panel['title']) + '\n\n'
        if kind == 'navigation':
            if not isinstance(panel['groups'], list) or not panel['groups']:
                raise ValueError('Navigation needs existing useful groups')
            for group in panel['groups']:
                if not isinstance(group, dict) or set(group) != {'title', 'items'} or not isinstance(group['items'], list) or not group['items']:
                    raise ValueError('Empty or invalid navigation group')
                text += '**' + line(group['title']) + '**\n\n'
                for item in group['items']:
                    if not isinstance(item, dict) or set(item) != {'label', 'map'}:
                        raise ValueError('Invalid navigation item')
                    text += '- [[' + vault_map(item['map']) + '|' + line(item['label']) + ']]\n'
                text += '\n'
        else:
            if not isinstance(panel['body'], str) or not panel['body'].strip():
                raise ValueError('Legend needs actual notation')
            text += panel['body']
        if kind == 'navigation':
            text = mark_current_navigation(text, current_map)
        frame = document_node(nodes, panel['id'], text.rstrip(), panel['placement'], kind)
        canvas['nodes'].append(frame); audit['panels'].append(copy.deepcopy(frame))


def review_composition(canvas, audit):
    """Unreviewed reverse connectors are review candidates, never automatic deletions."""
    nodes = indexed(canvas['nodes'])
    return {'returnReferences': len(audit.get('returns', [])),
            'orientationPanels': len(audit.get('panels', [])),
            'reverseEdgesToReview': [e['id'] for e in canvas['edges']
                                     if nodes[e['toNode']]['x'] < nodes[e['fromNode']]['x']],
            'boundary': 'Review semantic necessity and rendered readability; not a zero-reverse-edge gate'}


def assert_preserved(original, projected, audit):
    """Independent collapse check: exact original fields, order and branches."""
    recovered = copy.deepcopy(projected)
    nodes, edges = indexed(recovered['nodes']), indexed(recovered['edges'])
    removed = set()
    return_edges = {}
    for record in audit.get('returns', []):
        frame, leg, edge = record['frame'], record['leg'], record['originalEdge']
        if nodes.get(frame['id']) != frame or edges.get(leg['id']) != leg:
            raise ValueError('Changed return reference or relation')
        if record['targetId'] != edge['toNode'] or leg['fromNode'] != edge['fromNode']:
            raise ValueError('Changed return target or origin')
        removed.add(frame['id']); return_edges[leg['id']] = edge
    for panel in audit.get('panels', []):
        if nodes.get(panel['id']) != panel:
            raise ValueError('Changed orientation panel')
        removed.add(panel['id'])
    recovered['nodes'] = [n for n in recovered['nodes'] if n['id'] not in removed]
    recovered['edges'] = [return_edges.get(e['id'], e) for e in recovered['edges']]
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
    if not isinstance(spec, dict) or set(spec) - {'sourceSha256', 'nodeKinds', 'edgeKinds', 'placements', 'composition'}:
        raise ValueError('Unknown edit-spec fields')
    data = source.read_bytes()
    if hashlib.sha256(data).hexdigest() != spec.get('sourceSha256'):
        raise ValueError('Source changed; review current creator edits first')
    audit_path = output.with_suffix(output.suffix + '.projection.json')
    if output.exists() or output.is_symlink() or audit_path.exists() or audit_path.is_symlink():
        raise ValueError('Refuse to overwrite input, output or audit')
    original = json.loads(data)
    canvas, audit = project(original, spec.get('nodeKinds'), spec.get('edgeKinds'), spec.get('placements'), spec.get('composition'))
    audit['sourceSha256'] = spec['sourceSha256']
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8') as f:
        f.write(json.dumps(canvas, ensure_ascii=False, indent=2) + '\n')
    with audit_path.open('x', encoding='utf-8') as f:
        f.write(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
    return canvas, audit


def check_entry_guard(canvas, entry, launch, guard):
    """Check explicit local paths, not the meaning/authority of the supplied guard."""
    nodes = indexed(canvas['nodes']); edges = indexed(canvas['edges'])
    if len({entry, launch, guard}) != 3 or not {entry, launch, guard} <= nodes.keys():
        raise ValueError('Entry, launch and guard must be distinct existing nodes')
    graph = {key: [] for key in nodes}
    for edge in edges.values():
        if edge['fromNode'] not in nodes or edge['toNode'] not in nodes:
            raise ValueError('Dangling edge')
        graph[edge['fromNode']].append(edge['toNode'])

    def reachable(start, target, blocked=None):
        pending = [start]; visited = set()
        while pending:
            key = pending.pop()
            if key == blocked or key in visited:
                continue
            if key == target:
                return True
            visited.add(key); pending.extend(graph[key])
        return False

    if not reachable(entry, guard) or not reachable(guard, launch):
        raise ValueError('Declared guard does not lie on an entry-to-launch path')
    if reachable(entry, launch, blocked=guard):
        raise ValueError('An entry-to-launch path bypasses the declared guard')
    return {'entry': entry, 'launch': launch, 'guard': guard,
            'scope': 'explicit local graph only; inspect guard meaning, state branches and other entries separately'}


def check_entry_cli(argv):
    p = argparse.ArgumentParser(description='Check a declared local entry guard; not product-policy inference.')
    p.add_argument('source', type=Path)
    for option in ('entry', 'launch', 'guard'):
        p.add_argument('--' + option, required=True)
    args = p.parse_args(argv)
    try:
        result = check_entry_guard(json.loads(args.source.read_text(encoding='utf-8')),
                                   args.entry, args.launch, args.guard)
    except (ValueError, KeyError, OSError) as exc:
        p.exit(1, 'ERROR: ' + str(exc) + '\n')
    print(json.dumps(result))


def reader_inventory(canvas):
    """Lossless raw text plus alias-resolved reading text; no acceptance inference."""
    indexed(canvas['nodes'])
    cards = []
    for node in canvas['nodes']:
        raw = node.get('text', node.get('label', ''))
        if not raw:
            continue
        # Leave embeds intact: their visible content requires rendered inspection.
        display = re.sub(r'(?<!!)\[\[([^\]\n]+)\]\]',
                         lambda m: m[1].split('|', 1)[-1], raw)
        cards.append({'id': node['id'], 'type': node['type'],
                      'role': node.get('fab', {}).get('kind'),
                      'rawText': raw, 'readingText': display})
    encoded = json.dumps(canvas, ensure_ascii=False, sort_keys=True).encode('utf-8')
    return {'schemaVersion': 1, 'canvasSha256': hashlib.sha256(encoded).hexdigest(),
            'cards': cards, 'editorialReview': 'not assessed',
            'nativeFit': 'unverified',
            'scope': 'text inventory; linked files and embedded assets require separate inspection'}


def review_text_cli(argv):
    p = argparse.ArgumentParser(description='Extract complete Canvas reader text; no semantic/native PASS.')
    p.add_argument('source', type=Path); p.add_argument('output', type=Path)
    args = p.parse_args(argv)
    if args.output.exists() or args.output.is_symlink():
        p.exit(1, 'ERROR: Refuse to overwrite an existing review inventory\n')
    try:
        inventory = reader_inventory(json.loads(args.source.read_text(encoding='utf-8')))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x', encoding='utf-8') as f:
            f.write(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n')
    except (ValueError, KeyError, OSError) as exc:
        p.exit(1, 'ERROR: ' + str(exc) + '\n')
    print(json.dumps({'output': str(args.output), 'cards': len(inventory['cards']),
                      'editorialReview': inventory['editorialReview'], 'nativeFit': inventory['nativeFit']}))


# The producer shares role definitions with projection and legend authoring.
NOTATION = {
    'screen': ('Screen / state', 'Application surface and its current state.', '□'),
    'action': ('Action', 'A person initiates this transition.', '🟩'),
    'condition': ('Condition', 'A named condition selects the continuation.', '◇'),
    'result': ('Result', 'Outcome on the existing surface; not an extra screen.', '□'),
    'module': ('Shared module', 'Reused behavior with caller-specific entry and return.', '🟪'),
    'modal': ('Modal task', 'A temporary task above its originating surface.', '🟦'),
    'empty': ('Empty state', 'No data in the stated context; not a technical failure.', '◻'),
    'error': ('Action error', 'Failure with retained input and a recovery path.', '🟥'),
    'event': ('Service event', 'An external update, not a person pressing a control.', '🟨'),
    'continuation': ('Continuation / return', 'A named destination and retained context; not an extra app action.', '↪'),
}


def markdown_height(text, width, media_height=None):
    """Native-informed preparation, not a renderer or a native-fit verdict.

    Keep paragraph/rule/list spacing rather than measuring raw source lines.
    The profile follows observed default Canvas spacing. Unsupported embeds need
    an explicit rendered height; an arbitrary tiny fallback would hide clipping.
    """
    import unicodedata
    if not isinstance(text, str) or not isinstance(width, (int, float)) or width < 240:
        raise ValueError('Text and a card width of at least 240 are required')
    if '![' in text:
        if not isinstance(media_height, (int, float)) or media_height <= 0:
            raise ValueError('Embedded media needs an explicit measured mediaHeight')
    elif media_height is not None:
        raise ValueError('mediaHeight without embedded media')
    visible = re.sub(r'!?\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', lambda m: m[2] or m[1], text)
    visible = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', visible)
    height = 40 + (media_height or 0)
    for raw in visible.splitlines():
        if not raw.strip():
            height += 16
            continue
        if re.fullmatch(r'\s*(?:---+|\*\*\*+)\s*', raw):
            height += 64
            continue
        heading = bool(re.match(r'^#{1,6}\s', raw))
        bullet = bool(re.match(r'^\s*(?:[-*+] |\d+[.)] )', raw))
        content = re.sub(r'^#{1,6}\s+|^\s*(?:[-*+] |\d+[.)] )', '', raw)
        content = re.sub(r'[*_`]', '', content)
        available = width - (64 if bullet else 40)
        # Conservative variable-width em estimate, including Cyrillic and wide glyphs.
        size = 24 if heading else 18
        lines, advance = 1, 0
        for word in re.findall(r'\S+\s*', content):
            span = sum(size * (1 if unicodedata.east_asian_width(c) in ('W', 'F')
                              else .82 if c in 'MWЖШЩЮФ@' else .62) for c in word)
            if advance and advance + span > available:
                lines += 1; advance = 0
            extra = max(0, math.ceil(span / available) - 1)
            lines += extra
            advance = span - extra * available + advance
        height += lines * (34 if heading else 28)
    return math.ceil(max(88, height))


def display_id(value):
    """A stable reader-facing address, distinct from internal node keys."""
    if not isinstance(value, str) or not re.fullmatch(r'[A-Z]+-?\d+(?:[-.][A-Za-z0-9]+)*', value):
        raise ValueError('Expected a compact reader ID such as S01, A02 or E11')
    return value


def surface_body(card, cards, labels, require, edges=None, bindings=None):
    """Explicit visible composition; never infer interface fields from prose."""
    surface = card.get('surface')
    if surface is None:
        if require and card['kind'] in ('screen', 'modal', 'empty'):
            raise ValueError('Interface view requires explicit surface content and controls: ' + card['id'])
        return card.get('body', '')
    if card['kind'] not in ('screen', 'modal', 'empty') or not isinstance(surface, dict) or set(surface) != {'content', 'controls'}:
        raise ValueError('surface belongs to an actual screen/modal/empty state with content and controls')
    if not isinstance(surface['content'], list) or not surface['content'] or not isinstance(surface['controls'], list):
        raise ValueError('Visible content must be nonempty; controls may explicitly be empty for read-only states')
    content = [line(item) for item in surface['content']]
    controls = []
    for item in surface['controls']:
        if not isinstance(item, dict) or set(item) - {'label', 'target', 'kind', 'effect', 'reason'} or 'label' not in item:
            raise ValueError('Control needs a label and command/input/local/unresolved meaning')
        label = line(item['label'])
        kind = item.get('kind', 'command')
        target = item.get('target')
        if kind not in ('command', 'input', 'local', 'unresolved'):
            raise ValueError('Unknown control kind')
        if target is not None and (not isinstance(target, str) or target not in cards):
            raise ValueError('Unknown surface control target')
        if require:
            if kind == 'command':
                if target is None:
                    raise ValueError('Command needs an explicit action target: ' + card['id'] + ' / ' + label)
                if cards[target]['kind'] != 'action':
                    raise ValueError('Command target must be an action, not a module/surface/result')
                if not any(e['fromNode'] == card['id'] and e['toNode'] == target and e.get('kind') == 'forward' for e in (edges or [])):
                    raise ValueError('Command action is not owned by this surface')
                if not any(e['fromNode'] == target for e in (edges or [])):
                    raise ValueError('Command action has no represented continuation/outcome')
            elif kind in ('input', 'local'):
                if target is not None:
                    raise ValueError('Local input/effect cannot hide a graph command target')
                if kind == 'local':
                    line(item.get('effect'))
            else:
                if target is not None:
                    raise ValueError('Unresolved control cannot pretend to have an accepted target')
                line(item.get('reason'))
        if bindings is not None:
            bindings.append({'surface': card['id'], 'label': label, 'kind': kind,
                             **{k: item[k] for k in ('target', 'effect', 'reason') if k in item}})
        controls.append(label + (' → ' + display_id(cards[target]['displayId'])
                         if target is not None and cards[target].get('displayId') else ''))
    result = '**' + labels['content'] + '**\n\n' + '\n'.join('- ' + item for item in content)
    if controls:
        result += '\n\n---\n\n**' + labels['controls'] + '**\n\n' + '\n'.join('- ' + item for item in controls)
    if card.get('body'):
        result = '**' + labels['behavior'] + '**\n\n' + card['body'] + '\n\n---\n\n' + result
    return result


def expand_user_triggers(source):
    """Project explicitly declared commands; never infer a click from geometry."""
    spec = copy.deepcopy(source)
    cards, edges = indexed(spec['cards']), indexed(spec['edges'])
    ui = {'screen', 'modal', 'empty'}
    actions, replacements, audit, unresolved = {}, [], [], []
    for edge in edges.values():
        if edge['fromNode'] not in cards or edge['toNode'] not in cards:
            raise ValueError('Dangling producer edge')
        trigger = edge.get('trigger')
        direct_ui = (edge.get('kind') == 'forward' and cards[edge['fromNode']]['kind'] in ui
                     and cards[edge['toNode']]['kind'] in ui)
        if trigger is not None:
            if edge.get('kind') != 'forward' or edge.get('cause') is not None:
                raise ValueError('A user trigger needs a forward edge without a second cause')
            if not isinstance(trigger, dict) or set(trigger) != {'id', 'displayId', 'title'}:
                raise ValueError('trigger needs explicit id, displayId and title')
            key = line(trigger['id']); number = display_id(trigger['displayId'])
            card = dict(id=key, displayId=number, title=line(trigger['title']), kind='action',
                        lane=cards[edge['toNode']]['lane'])
            if key in cards:
                raise ValueError('Trigger action collides with an existing card')
            if key in actions and actions[key] != card:
                raise ValueError('Shared trigger has conflicting definitions')
            actions[key] = card
            first = {k: v for k, v in edge.items() if k not in ('trigger', 'label')}
            first['toNode'] = key
            exit_id = 'SF-trigger-out-' + key
            second = dict(id=exit_id, fromNode=key, toNode=edge['toNode'], kind='forward')
            if exit_id in edges:
                raise ValueError('Trigger exit ID collision')
            existing = next((e for e in replacements if e['id'] == exit_id), None)
            if existing is not None and existing != second:
                raise ValueError('Shared command must have the same actual continuation')
            replacements.append(first)
            if existing is None:
                replacements.append(second)
            audit.append({'originalEdge': copy.deepcopy(edge), 'actionId': key, 'exitEdgeId': exit_id})
        else:
            if spec.get('view', 'interface') == 'interface' and direct_ui:
                if edge.get('cause') not in ('automatic', 'input', 'external', 'unresolved') or not edge.get('reason'):
                    raise ValueError('Direct interface transition needs a user trigger or an explicit justified cause: ' + edge['id'])
                line(edge['reason'])
                if edge['cause'] == 'unresolved':
                    unresolved.append(copy.deepcopy(edge))
            replacements.append(copy.deepcopy(edge))
    spec['cards'].extend(actions.values())
    spec['edges'] = replacements
    return spec, audit, unresolved


def project_legend(specs):
    """Derive one notation contract from the entire explicitly supplied project."""
    if not isinstance(specs, list) or not specs:
        raise ValueError('Project legend needs the complete nonempty map spec list')
    roles, families, notation, paths = set(), {}, {}, set()
    for source in specs:
        path = vault_map(source['mapPath'])
        if path in paths:
            raise ValueError('Duplicate map in project legend scope')
        paths.add(path)
        spec, _, _ = expand_user_triggers(source)
        entities = [(c['kind'], c.get('displayId')) for c in spec['cards']]
        entities += [('continuation', e.get('displayId')) for e in spec['edges'] if e.get('kind') == 'return']
        for kind, number in entities:
            if kind not in NOTATION:
                raise ValueError('Unknown project notation role')
            roles.add(kind)
            if number:
                families.setdefault(kind, set()).add(re.match(r'[A-Z]+', display_id(number))[0])
        for kind, value in source.get('notation', {}).items():
            if kind in notation and notation[kind] != value:
                raise ValueError('Conflicting project notation definitions')
            notation[kind] = copy.deepcopy(value)
    return {'roles': [kind for kind in NOTATION if kind in roles],
            'families': {kind: sorted(families.get(kind, set())) for kind in roles},
            'notation': notation}


def produce_project(specs):
    """Use the same project-wide legend on every map; no hidden vault scan."""
    legend = project_legend(specs)
    result = []
    for source in specs:
        spec = copy.deepcopy(source)
        spec['projectLegend'] = legend
        result.append(produce(spec))
    return result


def produce(spec):
    """Produce a new Canvas from explicit cards, lanes and typed relations.

    Forward topology determines columns globally; lanes never restart columns.
    No product behavior, modules, phases or grouping are inferred. Returns retain
    their original relation in evidence and use named documentary continuations.
    """
    if set(spec) - {'cards', 'edges', 'mapPath', 'notation', 'navigation', 'labels', 'view', 'layout', 'projectLegend'}:
        raise ValueError('Unknown producer fields')
    source_spec = copy.deepcopy(spec)
    spec, trigger_audit, unresolved = expand_user_triggers(spec)
    cards, edges = indexed(spec['cards']), indexed(spec['edges'])
    view = spec.get('view', 'interface')
    if view not in ('interface', 'behavior'):
        raise ValueError('view must be interface or behavior')
    layout = dict(columnGap=400, laneGap=160)
    if set(spec.get('layout', {})) - set(layout):
        raise ValueError('Unknown layout option')
    layout.update(spec.get('layout', {}))
    if any(type(v) not in (int, float) or not math.isfinite(v) or v < 100 for v in layout.values()):
        raise ValueError('Layout gaps must be finite and at least 100')
    if not cards:
        raise ValueError('At least one card required')
    map_path = vault_map(spec['mapPath'])
    labels = dict(legend='Notation', navigation='Navigation', target='Target ID',
                  continuation='Continue at the named destination', content='Visible content',
                  controls='Controls', behavior='Behavior and recovery')
    if set(spec.get('labels', {})) - set(labels):
        raise ValueError('Unknown producer labels')
    labels.update({k: line(v) for k, v in spec.get('labels', {}).items()})
    roles = {k: {'label': v[0], 'description': v[1], 'symbol': v[2]} for k, v in NOTATION.items()}
    for kind, value in spec.get('notation', {}).items():
        if kind not in roles or set(value) != {'label', 'description'}:
            raise ValueError('Notation requires a known role, label and description')
        roles[kind].update({k: line(v) for k, v in value.items()})
    display_ids = set()
    for entity in list(cards.values()) + [e for e in edges.values() if e.get('kind') == 'return']:
        value = entity.get('displayId')
        if value is None:
            if view == 'interface':
                raise ValueError('Interface view requires stable displayId on every semantic node and return')
        elif display_id(value) in display_ids:
            raise ValueError('Duplicate reader displayId')
        else:
            display_ids.add(value)
    project = spec.get('projectLegend')
    if project is not None:
        if not isinstance(project, dict) or set(project) != {'roles', 'families', 'notation'}:
            raise ValueError('Invalid project legend contract')
        if (not isinstance(project['roles'], list) or len(project['roles']) != len(set(project['roles']))
                or not set(project['roles']) <= set(NOTATION)):
            raise ValueError('Invalid project legend roles')
        for kind, value in project['notation'].items():
            if kind not in roles or set(value) != {'label', 'description'}:
                raise ValueError('Invalid project role definition')
            roles[kind].update({k: line(v) for k, v in value.items()})
    graph = {k: [] for k in cards}; indegree = dict.fromkeys(cards, 0)
    for card in cards.values():
        if card.get('kind') not in roles or card['kind'] == 'continuation':
            raise ValueError('Unknown card role; continuations are produced from return edges')
        if type(card.get('lane')) is not int or card['lane'] < 0:
            raise ValueError('Each card needs an explicit nonnegative lane')
    for edge in edges.values():
        if edge['fromNode'] not in cards or edge['toNode'] not in cards:
            raise ValueError('Dangling producer edge')
        if edge.get('kind') not in ('forward', 'return'):
            raise ValueError('Every edge needs explicit forward/return meaning')
        if edge['kind'] == 'forward':
            graph[edge['fromNode']].append(edge['toNode']); indegree[edge['toNode']] += 1
        elif not edge.get('retained') or not edge.get('label'):
            raise ValueError('Return requires a meaningful label and retained context')
    if view == 'interface':
        for card in cards.values():
            if (card['kind'] == 'module'
                    and any(e['toNode'] == card['id'] for e in edges.values())
                    and not any(e['fromNode'] == card['id'] for e in edges.values())):
                raise ValueError('Invoked module needs a represented caller continuation/outcome: ' + card['id'])
    ranks = dict.fromkeys(cards, 0); pending = [k for k in cards if not indegree[k]]; visited = []
    while pending:
        key = pending.pop(0); visited.append(key)
        for target in graph[key]:
            ranks[target] = max(ranks[target], ranks[key] + 1)
            indegree[target] -= 1
            if not indegree[target]:
                pending.append(target)
    if len(visited) != len(cards):
        raise ValueError('Forward cycle: classify actual recovery/return separately; do not drop it')
    placed, occupied, control_bindings = [], set(), []
    for key, card in cards.items():
        slot = ranks[key], card['lane']
        if slot in occupied:
            raise ValueError('Two cards share a column/lane; declare a distinct meaningful lane')
        occupied.add(slot)
        width = card.get('width', 260 if card['kind'] == 'action' else 460)
        body = surface_body(card, cards, labels, view == 'interface', list(edges.values()), control_bindings)
        caption = card.get('caption')
        if card.get('displayId'):
            caption = card['displayId'] + ' · ' + roles[card['kind']]['label'] + (' · ' + caption if caption else '')
        text = card_text(card['title'], body, caption)
        height = max(markdown_height(text, width, card.get('mediaHeight')), card.get('minHeight', 0))
        node = dict(id=key, type='text', text=text, width=width, height=height,
                    fab={'kind': card['kind'], 'lane': card['lane'], 'column': ranks[key], 'displayId': card.get('displayId')})
        if PALETTE[card['kind']] is not None:
            node['color'] = PALETTE[card['kind']]
        placed.append(node)
    output_edges, returns = [], []
    next_lane = max(c['lane'] for c in cards.values()) + 1
    for edge in edges.values():
        leg = {k: v for k, v in edge.items() if k not in ('kind', 'retained', 'displayId')}
        leg.update(fromSide='right', toSide='left', toEnd='arrow')
        if edge['kind'] == 'return':
            target = cards[edge['toNode']]
            text = continuation_text(edge['label'], map_path, target['id'], target['title'], edge['retained'], labels['target'],
                                     target_display_id=target.get('displayId'),
                                     caption=edge['displayId'] + ' · ' + roles['continuation']['label'] if edge.get('displayId') else None)
            key = 'SF-return-' + edge['id']
            if key in cards:
                raise ValueError('Return ID collision')
            placed.append(dict(id=key, type='text', text=text, width=460,
                               height=markdown_height(text, 460),
                               fab={'kind': 'continuation', 'lane': next_lane,
                                    'column': ranks[edge['fromNode']] + 1, 'displayId': edge.get('displayId')}))
            next_lane += 1
            leg['toNode'] = key
            leg.pop('label', None)  # Already rendered as the continuation title.
            returns.append(copy.deepcopy(edge))
        output_edges.append(leg)
    # Columns own collision resolution. A tall unrelated card cannot stretch an
    # entire row across the map. Lanes retain branch order, not absolute Y slots.
    col_width = {}
    for node in placed:
        col = node['fab']['column']
        col_width[col] = max(col_width.get(col, 0), node['width'])
    xs, offset = {}, 0
    for col in range(max(col_width) + 1):
        xs[col] = offset
        offset += col_width.get(col, 460) + layout['columnGap']
    by_id = indexed(placed)
    predecessors = {key: [] for key in by_id}
    for edge in output_edges:
        predecessors[edge['toNode']].append(edge['fromNode'])
    for col in sorted(col_width):
        column = sorted((n for n in placed if n['fab']['column'] == col),
                        key=lambda n: n['fab']['lane'])
        bottom = None
        for node in column:
            sources = [by_id[key] for key in predecessors[node['id']]]
            same_lane = [n for n in sources if n['fab']['lane'] == node['fab']['lane']]
            if same_lane:
                # Preserve the nearest explicit continuation on this branch.
                anchor = max(same_lane, key=lambda n: n['fab']['column'])
                centre = anchor['y'] + anchor['height'] / 2
            elif sources:
                centres = sorted(n['y'] + n['height'] / 2 for n in sources)
                centre = centres[len(centres) // 2]
            else:
                centre = node['height'] / 2
            preferred = centre - node['height'] / 2
            y = preferred if bottom is None else max(preferred, bottom + layout['laneGap'])
            node.update(x=xs[col], y=y)
            bottom = y + node['height']
    # One translation preserves all relative positions while keeping Y nonnegative.
    minimum = min(n['y'] for n in placed)
    if minimum < 0:
        for node in placed:
            node['y'] -= minimum
    used = list(dict.fromkeys(n['fab']['kind'] for n in placed))
    legend_roles = project['roles'] if project is not None else used
    if not set(used) <= set(legend_roles):
        raise ValueError('Project legend omits a role used by this map')
    assets = {}
    legend_lines = []
    for kind in legend_roles:
        color = PALETTE.get(kind)
        asset = str(Path(map_path).parent / 'assets' / ('sf-' + kind + '.svg'))
        assets[asset] = ('event' if kind == 'condition' else kind) if color is not None else 'neutral'
        prefix = '![[' + asset + '|12]] '
        family = sorted({re.match(r'[A-Z]+', n['fab']['displayId'])[0] for n in placed
                         if n['fab']['kind'] == kind and n['fab'].get('displayId')})
        if project is not None:
            family = project['families'].get(kind, [])
        name = ('/'.join(family) + ' — ' if family else '') + roles[kind]['label']
        legend_lines.append(prefix + '**' + name + '** — ' + roles[kind]['description'])
    panels = []
    if spec.get('navigation'):
        panels.append(('SF-navigation', card_text(labels['navigation'], mark_current_navigation(spec['navigation'], map_path)), 'navigation', None))
    panels.append(('SF-legend', '## ' + labels['legend'] + '\n\n' + '\n\n'.join(legend_lines), 'legend', 12 if assets else None))
    panel_y = 0
    for key, text, kind, media in panels:
        if key in cards or any(n['id'] == key for n in placed):
            raise ValueError('Orientation ID collision')
        height = markdown_height(text, 460, media)
        placed.append(dict(id=key, type='text', text=text, x=-860, y=panel_y,
                           width=460, height=height, fab={'kind': kind}))
        panel_y += height + 100
    canvas = {'nodes': placed, 'edges': output_edges}
    return canvas, {'schemaVersion': 1, 'nativeFit': 'unverified',
                    'sourceSpecSha256': hashlib.sha256(json.dumps(source_spec, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
                    'userTriggers': trigger_audit, 'unresolvedTransitions': unresolved,
                    'controlBindings': control_bindings,
                    'unresolvedControls': [c for c in control_bindings if c['kind'] == 'unresolved'],
                    'returnRelations': returns, 'usedRoles': used, 'assets': assets,
                    'legendRoles': legend_roles, 'legendScope': 'project' if project is not None else 'single-map only',
                    'displayIds': {n['id']: n['fab']['displayId'] for n in placed if n['fab'].get('displayId')},
                    'view': view, 'interfaceComposition': 'explicit authored content; not independently accepted' if view == 'interface' else 'not an interface projection',
                    'scope': 'explicit topology/lane composition and estimated Markdown fit; inspect exact native revision'}


def write_producer_assets(output_dir, audit):
    """Copy bundled swatches next to output; identical existing assets are safe."""
    bundled = Path(__file__).resolve().parent.parent / 'assets' / 'screen-flow'
    for name, kind in audit.get('assets', {}).items():
        data = (bundled / (kind + '.svg')).read_bytes()
        destination = Path(output_dir) / 'assets' / Path(name).name
        if destination.parent.is_symlink() or destination.is_symlink():
            raise ValueError('Refuse symlinked producer asset destination')
        if destination.exists() and destination.read_bytes() != data:
            raise ValueError('Refuse conflicting existing swatch')
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            destination.write_bytes(data)


def produce_cli(argv):
    p = argparse.ArgumentParser(description='Produce a new Canvas from explicit topology and lanes.')
    p.add_argument('spec', type=Path); p.add_argument('output', type=Path)
    args = p.parse_args(argv)
    audit_path = args.output.with_suffix('.canvas.producer.json')
    if args.output.exists() or audit_path.exists() or args.output.is_symlink() or audit_path.is_symlink():
        p.exit(1, 'ERROR: Refuse to overwrite output or evidence\n')
    canvas, audit = produce(json.loads(args.spec.read_text(encoding='utf-8')))
    write_producer_assets(args.output.parent, audit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(canvas, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'cards': len(canvas['nodes']), 'nativeFit': audit['nativeFit']}))


def main():
    import sys
    if sys.argv[1:2] == ['produce']:
        return produce_cli(sys.argv[2:])
    if sys.argv[1:2] == ['check-entry']:
        return check_entry_cli(sys.argv[2:])
    if sys.argv[1:2] == ['review-text']:
        return review_text_cli(sys.argv[2:])
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path); p.add_argument('output', type=Path)
    p.add_argument('--spec', type=Path, required=True)
    args = p.parse_args()
    try:
        canvas, audit = write_projection(args.source, args.output, json.loads(args.spec.read_text()))
    except (ValueError, KeyError) as exc:
        p.exit(1, 'ERROR: ' + str(exc) + '\n')
    print(json.dumps({'output': str(args.output), 'frames': len(audit['frames']),
                      'nodes': len(canvas['nodes']), 'compositionReview': review_composition(canvas, audit), 'scope': 'static reversible projection; native fit unknown'}))


if __name__ == '__main__':
    main()
