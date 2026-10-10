#!/usr/bin/env python3
"""Render an approximate full-canvas SVG preview from Obsidian Canvas JSON.

The preview is for quick layout QA when Obsidian is unavailable. Obsidian's
own rendering remains the review surface.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import textwrap
from pathlib import Path


COLORS = {
    '1': '#fce8e8', '2': '#fcebdc', '3': '#fff3ce',
    '4': '#e5f2e8', '5': '#e2f2f4', '6': '#ece7fa',
}


def node_fill(node: dict, default: str = '#fff') -> str:
    color = str(node.get('color', ''))
    if re.fullmatch(r'#[0-9a-fA-F]{6}', color):
        return color
    return COLORS.get(color, default)


def anchor(node: dict, side: str) -> tuple[float, float]:
    x, y, w, h = (float(node[key]) for key in ('x', 'y', 'width', 'height'))
    return {
        'left': (x, y + h / 2), 'right': (x + w, y + h / 2),
        'top': (x + w / 2, y), 'bottom': (x + w / 2, y + h),
    }.get(side, (x + w / 2, y + h / 2))


def label_lines(node: dict) -> list[str]:
    value = (node.get('label', '') if node.get('type') == 'group'
             else node.get('text') or ('↗ ' + str(node.get('file', ''))))
    if node.get('type') == 'group':
        return [textwrap.shorten(value, width=max(12, int(float(node['width']) / 13)), placeholder='…')] if value else []
    lines: list[str] = []
    max_chars = max(12, int(float(node['width']) / 13))
    for raw in value.splitlines():
        clean = raw.lstrip('# ').strip()
        if not clean:
            continue
        lines.extend(textwrap.wrap(clean, width=max_chars, break_long_words=False)
                     or [clean])
    return lines[:8]


def contains(group: dict, child: dict) -> bool:
    return (group.get('type') == 'group'
            and float(group['x']) <= float(child['x'])
            and float(group['y']) <= float(child['y'])
            and float(group['x']) + float(group['width']) >= float(child['x']) + float(child['width'])
            and float(group['y']) + float(group['height']) >= float(child['y']) + float(child['height']))


def layout_warnings(canvas: dict) -> list[str]:
    nodes = canvas.get('nodes', [])
    warnings: list[str] = []
    for index, a in enumerate(nodes):
        for b in nodes[index + 1:]:
            left = max(float(a['x']), float(b['x']))
            top = max(float(a['y']), float(b['y']))
            right = min(float(a['x']) + float(a['width']),
                        float(b['x']) + float(b['width']))
            bottom = min(float(a['y']) + float(a['height']),
                         float(b['y']) + float(b['height']))
            if right > left and bottom > top:
                if not contains(a, b) and not contains(b, a):
                    warnings.append(f'overlapping nodes: {a["id"]}, {b["id"]}')
        if a.get('type') != 'group' and (node_lines := label_lines(a)):
            if 32 + 25 * (len(node_lines) - 1) > float(a['height']) - 10:
                warnings.append(f'text may overflow node: {a["id"]}')
    # Obsidian places group titles above the frame, not inside it.
    for group in nodes:
        if group.get('type') != 'group' or not group.get('label'):
            continue
        header = dict(group, y=float(group['y']) - 50, height=50)
        for other in nodes:
            if other['id'] == group['id'] or contains(other, group):
                continue
            if (max(float(header['x']), float(other['x'])) < min(float(header['x']) + float(header['width']), float(other['x']) + float(other['width']))
                    and max(float(header['y']), float(other['y'])) < min(float(header['y']) + 50, float(other['y']) + float(other['height']))):
                warnings.append(f'group title overlaps node: {group["id"]}, {other["id"]}')
    return warnings


def render(canvas: dict) -> str:
    nodes = canvas.get('nodes', [])
    edges = canvas.get('edges', [])
    if not nodes:
        raise ValueError('Canvas has no nodes')
    by_id = {node['id']: node for node in nodes}
    min_x = min(float(n['x']) for n in nodes) - 60
    min_y = min(float(n['y']) for n in nodes) - 60
    max_x = max(float(n['x']) + float(n['width']) for n in nodes) + 60
    max_y = max(float(n['y']) + float(n['height']) for n in nodes) + 60
    width, height = max_x - min_x, max_y - min_y
    display_width = min(1800, int(width))
    display_height = max(1, round(display_width * height / width))
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{display_width}" '
        f'height="{display_height}" viewBox="{min_x:g} {min_y:g} {width:g} {height:g}">',
        '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" '
        'refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" '
        'fill="#636b74"/></marker></defs>',
        f'<rect x="{min_x:g}" y="{min_y:g}" width="{width:g}" '
        f'height="{height:g}" fill="#fbfbfa"/>',
    ]
    # Containers go behind edges and contents regardless of JSON node order.
    groups = sorted((n for n in nodes if n.get('type') == 'group'),
                    key=lambda n: float(n['width']) * float(n['height']), reverse=True)
    for node in groups:
        x, y, w, h = (float(node[key]) for key in ('x', 'y', 'width', 'height'))
        parts.append(f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" '
                     f'rx="12" fill="{node_fill(node, "#f5f5f5")}" '
                     'stroke="#59616d" stroke-width="3"/>')
        for index, line in enumerate(label_lines(node)):
            parts.append(f'<text x="{x:g}" y="{y-12:g}" font-size="21" '
                         f'font-family="Arial, sans-serif">{html.escape(line)}</text>')
    for edge in edges:
        start = by_id.get(edge.get('fromNode'))
        end = by_id.get(edge.get('toNode'))
        if not start or not end:
            continue
        x1, y1 = anchor(start, edge.get('fromSide', 'right'))
        x2, y2 = anchor(end, edge.get('toSide', 'left'))
        parts.append(f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" '
                     f'y2="{y2:g}" stroke="#777e87" stroke-width="2.5" '
                     'marker-end="url(#arrow)"/>')
        label = str(edge.get('label', '')).strip()
        if label:
            cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
            label_width = min(280, max(60, len(label) * 11))
            parts.append(f'<rect x="{cx-label_width/2:g}" y="{cy-18:g}" '
                         f'width="{label_width:g}" height="30" rx="5" '
                         'fill="#fff" stroke="#ddd"/>')
            parts.append(f'<text x="{cx:g}" y="{cy+3:g}" text-anchor="middle" '
                         f'font-size="18" font-family="Arial, sans-serif" '
                         f'fill="#30343a">{html.escape(label)}</text>')
    for node in nodes:
        if node.get('type') == 'group':
            continue
        x, y, w, h = (float(node[key]) for key in ('x', 'y', 'width', 'height'))
        is_file = node.get('type') == 'file'
        fill = node_fill(node, '#f1f1f3' if is_file else '#fff')
        parts.append(f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" '
                     f'rx="12" fill="{fill}" stroke="#59616d" stroke-width="3"/>')
        for index, line in enumerate(label_lines(node)):
            text_y = y + 32 + index * 25
            if text_y > y + h - 10:
                break
            parts.append(f'<text x="{x+16:g}" y="{text_y:g}" font-size="21" '
                         f'font-family="Arial, sans-serif" fill="#1d2227">'
                         f'{html.escape(line)}</text>')
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'


def render_png(canvas: dict, output: Path) -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError as exc:
        raise SystemExit('PNG preview requires Pillow; use an .svg output instead') from exc
    nodes = canvas.get('nodes', [])
    if not nodes:
        raise ValueError('Canvas has no nodes')
    by_id = {node['id']: node for node in nodes}
    min_x = min(float(n['x']) for n in nodes) - 60
    min_y = min(float(n['y']) for n in nodes) - 60
    max_x = max(float(n['x']) + float(n['width']) for n in nodes) + 60
    max_y = max(float(n['y']) + float(n['height']) for n in nodes) + 60
    scale = 1.25
    image = Image.new('RGB', (round((max_x - min_x) * scale),
                              round((max_y - min_y) * scale)), '#fbfbfa')
    draw = ImageDraw.Draw(image)
    font_path = Path('/System/Library/Fonts/Supplemental/Arial Unicode.ttf')
    if not font_path.exists():
        font_path = Path('/System/Library/Fonts/Supplemental/Arial.ttf')
    font = ImageFont.truetype(str(font_path), round(21 * scale)) if font_path.exists() else ImageFont.load_default()
    edge_font = ImageFont.truetype(str(font_path), round(18 * scale)) if font_path.exists() else ImageFont.load_default()

    def pos(point: tuple[float, float]) -> tuple[int, int]:
        return (round((point[0] - min_x) * scale),
                round((point[1] - min_y) * scale))

    groups = sorted((n for n in nodes if n.get('type') == 'group'),
                    key=lambda n: float(n['width']) * float(n['height']), reverse=True)
    for node in groups:
        x, y, w, h = (float(node[key]) for key in ('x', 'y', 'width', 'height'))
        p1, p2 = pos((x, y)), pos((x+w, y+h))
        draw.rounded_rectangle((p1, p2), radius=14,
                               fill=node_fill(node, '#f5f5f5'),
                               outline='#59616d', width=4)
        for index, line in enumerate(label_lines(node)):
            draw.text((p1[0], p1[1]-round(40*scale)),
                      line, font=font, fill='#1d2227')
    for edge in canvas.get('edges', []):
        start = by_id.get(edge.get('fromNode'))
        end = by_id.get(edge.get('toNode'))
        if not start or not end:
            continue
        a = pos(anchor(start, edge.get('fromSide', 'right')))
        b = pos(anchor(end, edge.get('toSide', 'left')))
        draw.line((a, b), fill='#777e87', width=3)
        label = str(edge.get('label', '')).strip()
        if label:
            cx, cy = (a[0] + b[0]) // 2, (a[1] + b[1]) // 2
            box = draw.textbbox((cx, cy), label, font=edge_font, anchor='mm')
            draw.rounded_rectangle((box[0]-7, box[1]-4, box[2]+7, box[3]+4),
                                   radius=5, fill='#fff', outline='#ddd')
            draw.text((cx, cy), label, font=edge_font, fill='#30343a', anchor='mm')
        dx, dy = b[0]-a[0], b[1]-a[1]
        length = max(1, (dx*dx+dy*dy) ** .5)
        ux, uy = dx/length, dy/length
        left = (round(b[0]-12*ux-6*uy), round(b[1]-12*uy+6*ux))
        right = (round(b[0]-12*ux+6*uy), round(b[1]-12*uy-6*ux))
        draw.polygon((b, left, right), fill='#777e87')

    for node in nodes:
        if node.get('type') == 'group':
            continue
        x, y, w, h = (float(node[key]) for key in ('x', 'y', 'width', 'height'))
        p1 = pos((x, y))
        p2 = pos((x+w, y+h))
        fill = node_fill(node, '#f1f1f3' if node.get('type') == 'file' else '#fff')
        draw.rounded_rectangle((p1, p2), radius=14, fill=fill,
                               outline='#59616d', width=4)
        for index, line in enumerate(label_lines(node)):
            text_y = p1[1] + round((23 + 25 * index) * scale)
            if text_y > p2[1] - round(12 * scale):
                break
            draw.text((p1[0]+round(15*scale), text_y), line,
                      font=font, fill='#1d2227')
    image.save(output)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('canvas', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    data = json.loads(args.canvas.read_text(encoding='utf-8'))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.suffix.lower() == '.png':
        render_png(data, args.output)
    else:
        args.output.write_text(render(data), encoding='utf-8')
    print(args.output)
    for warning in layout_warnings(data):
        print(f'WARNING: {warning}')


if __name__ == '__main__':
    main()
