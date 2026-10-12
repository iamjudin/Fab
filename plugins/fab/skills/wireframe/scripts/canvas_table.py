#!/usr/bin/env python3
"""Readable Canvas inventory; semantic review remains separate."""
import argparse
import html
import json
from pathlib import Path


def cell(value):
    return html.escape(str(value), quote=False).replace('|', '&#124;').replace('`', '&#96;').replace('\r', '').replace('\n', '<br>')


def render(data):
    nodes, edges = data.get('nodes', []), data.get('edges', [])
    ids = [n['id'] for n in nodes]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate node IDs')
    if any(e['fromNode'] not in ids or e['toNode'] not in ids for e in edges):
        raise ValueError('Dangling edge')
    edge_ids = [e['id'] for e in edges]
    if len(set(edge_ids)) != len(edge_ids):
        raise ValueError('Duplicate edge IDs')
    groups = [n for n in nodes if n['type'] == 'group']
    lines = ['# Структура и переходы', '',
             'Инвентаризация исходной карты. Геометрические группы не доказывают смыслового владельца.', '',
             '| ID | Тип | Геометрические группы | Содержание / ссылка | Цвет |',
             '| --- | --- | --- | --- | --- |']
    for node in nodes:
        owners = [g['id'] for g in groups if g['id'] != node['id'] and
                  g['x'] <= node['x'] and g['y'] <= node['y'] and
                  node['x'] + node['width'] <= g['x'] + g['width'] and
                  node['y'] + node['height'] <= g['y'] + g['height']]
        content = '\n'.join(f'{key}: {node[key]}' for key in ('label', 'text', 'file', 'subpath', 'url') if key in node)
        row = [node['id'], node['type'], ', '.join(owners) or '—', content, node.get('color', '—')]
        lines.append('| ' + ' | '.join(cell(v) for v in row) + ' |')
    lines += ['', '| ID перехода | Откуда | Куда | Условие / действие | Направление концов |',
              '| --- | --- | --- | --- | --- |']
    for edge in edges:
        ends = f"{edge.get('fromEnd', 'none')} → {edge.get('toEnd', 'arrow')}"
        lines.append('| ' + ' | '.join(cell(v) for v in
                     [edge['id'], edge['fromNode'], edge['toNode'], edge.get('label', '—'), ends]) + ' |')
    # Escape fenced-code delimiters inside source strings while retaining JSON values.
    snapshot = json.dumps(data, ensure_ascii=False, indent=2).replace('`', '\\u0060')
    lines += ['', '## Полный исходный снимок', '', '```json', snapshot, '```', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.source.resolve() == args.output.resolve():
        parser.error('Output must not overwrite source')
    result = render(json.loads(args.source.read_text(encoding='utf-8')))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding='utf-8')
