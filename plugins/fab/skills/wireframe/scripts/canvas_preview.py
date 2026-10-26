#!/usr/bin/env python3
"""Render an approximate full-canvas SVG preview from Obsidian Canvas JSON.

The preview is for quick layout QA when Obsidian is unavailable. Obsidian's
own rendering remains the review surface.
"""

from __future__ import annotations

import argparse
import html
import heapq
import math
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
    return [row['text'] for row in text_layout(node) if row['kind'] != 'divider']


def setext_lines(value: str) -> tuple[set[int], set[int]]:
    """Recognize paragraph underlines relevant to card hierarchy; not a full parser."""
    lines = value.splitlines(); headings, underlines = set(), set()
    fenced = False
    for i, raw in enumerate(lines):
        clean = raw.strip()
        if clean.startswith(('```', '~~~')):
            fenced = not fenced
            continue
        if fenced or not re.fullmatch(r'(?:-{3,}|={3,})', clean) or not i:
            continue
        j = i - 1; paragraph = []
        while j >= 0 and lines[j].strip():
            prior = lines[j].strip()
            if re.match(r'^(?:#{1,6}\s|[-*+>]\s|\d+[.)]\s|[-=]{3,}$|```|~~~)', prior):
                break
            paragraph.append(j); j -= 1
        if paragraph:
            headings.update(paragraph); underlines.add(i)
    return headings, underlines


def text_layout(node: dict) -> list[dict]:
    """Small Markdown fallback, not an Obsidian renderer or font-fit proof."""
    value = node.get('text') or ('↗ ' + str(node.get('file', '')))
    rows, y, after_heading = [], 0, False
    setext, underlines = setext_lines(value)
    for index, raw in enumerate(value.splitlines()):
        if index in underlines:
            continue
        clean = raw.strip()
        if not clean:
            y += 6
            continue
        if re.fullmatch(r'(?:-{3,}|\*{3,}|_{3,})', clean):
            y += 8; rows.append(dict(kind='divider', text='', y=y, size=0, indent=0)); y += 6
            after_heading = False
            continue
        heading = index in setext or bool(re.match(r'^#{1,6}\s+', clean))
        clean = re.sub(r'^#{1,6}\s+', '', clean)
        clean = re.sub(r'!\[\[[^\]]+\]\]', '■', clean)
        clean = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', lambda m: m[2] or m[1], clean)
        clean = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', clean)
        clean = clean.replace('**', '').replace('`', '')
        bullet = bool(re.match(r'^[-*+]\s+', clean))
        if bullet: clean = '• ' + re.sub(r'^[-*+]\s+', '', clean)
        metadata = after_heading and (' · ' in clean or bool(re.match(r'^[A-Z]+[-\d]', clean)))
        size = 24 if heading else 18  # Plain Markdown captions have no guaranteed smaller native font.
        kind = 'heading' if heading else 'metadata' if metadata else 'body'
        columns = max(8, int((float(node['width']) - 32 - (14 if bullet else 0)) / (size * .6)))
        wrapped = textwrap.wrap(clean, width=columns, break_long_words=True) or [clean]
        for i, line in enumerate(wrapped):
            y += size + 4
            rows.append(dict(kind=kind, text=line, y=y, size=size, indent=14 if bullet and i else 0))
        after_heading = heading
    return rows


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
        if setext_lines(a.get('text', ''))[0]:
            warnings.append(f'setext heading changes card hierarchy: {a["id"]}')
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
        if a.get('type') != 'group' and (rows := text_layout(a)):
            if rows[-1]['y'] + 8 > float(a['height']) - 10:
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
    by_id={n['id']:n for n in nodes}
    for edge in canvas.get('edges',[]):
        if edge.get('fromNode') not in by_id or edge.get('toNode') not in by_id:continue
        route=edge_route(edge,by_id)
        for node in nodes:
            if node.get('type')=='group' or node['id'] in (edge['fromNode'],edge['toNode']):continue
            if any(segment_hits_box(a,b,node) for a,b in zip(route,route[1:])):
                warnings.append(f'edge crosses content: {edge["id"]}, {node["id"]}')
        label=str(edge.get('label','')).strip()
        if label:
            cx,cy,w=edge_label_position(route,label);box={'x':cx-w/2,'y':cy-18,'width':w,'height':30}
            for node in nodes:
                if node.get('type')=='group':continue
                if max(box['x'],float(node['x']))<min(box['x']+w,float(node['x'])+float(node['width'])) and max(box['y'],float(node['y']))<min(box['y']+30,float(node['y'])+float(node['height'])):
                    warnings.append(f'edge label overlaps content: {edge["id"]}, {node["id"]}')
    return warnings


def segment_hits_box(a, b, box):
    """Strict interior crossing; contact with an anchor's boundary is allowed."""
    x,y,w,h=(float(box[k]) for k in ('x','y','width','height'))
    x += 0.01; y += 0.01; w -= 0.02; h -= 0.02
    lo,hi=0.0,1.0
    for origin,delta,low,high in ((a[0],b[0]-a[0],x,x+w),(a[1],b[1]-a[1],y,y+h)):
        if abs(delta)<1e-9:
            if not low<origin<high:return False
        else:
            t1,t2=(low-origin)/delta,(high-origin)/delta
            lo=max(lo,min(t1,t2));hi=min(hi,max(t1,t2))
            if lo>=hi:return False
    return hi>0 and lo<1


def edge_route(edge, by_id):
    """Visibility-grid fallback around actual content, not a native Canvas claim."""
    start,end=by_id[edge['fromNode']],by_id[edge['toNode']]
    a,b=anchor(start,edge.get('fromSide','right')),anchor(end,edge.get('toSide','left'))
    obstacles=[n for n in by_id.values() if n['id'] not in (start['id'],end['id']) and n.get('type')!='group']
    # Source/target also obstruct intermediates; otherwise returns can cut through their own cards.
    boxes=obstacles+[start,end] if start.get('type')!='group' and end.get('type')!='group' else obstacles
    if not any(segment_hits_box(a,b,n) for n in boxes):return [a,b]
    xs={a[0],b[0]};ys={a[1],b[1]}
    for n in boxes:
        x,y,w,h=(float(n[k]) for k in ('x','y','width','height'))
        xs.update((x-22,x+w+22));ys.update((y-22,y+h+22))
    xs,ys=sorted(xs),sorted(ys)
    points={(i,j):(x,y) for i,x in enumerate(xs) for j,y in enumerate(ys)
            if (x,y) in (a,b) or not any(float(n['x'])<x<float(n['x'])+float(n['width']) and float(n['y'])<y<float(n['y'])+float(n['height']) for n in boxes)}
    source=(xs.index(a[0]),ys.index(a[1]));target=(xs.index(b[0]),ys.index(b[1]))
    costs={source:0};previous={};queue=[(0,source)]
    while queue:
        cost,point=heapq.heappop(queue)
        if cost!=costs[point]:continue
        if point==target:break
        for other in ((point[0]-1,point[1]),(point[0]+1,point[1]),(point[0],point[1]-1),(point[0],point[1]+1)):
            if other not in points:continue
            pa,pb=points[point],points[other]
            if any(segment_hits_box(pa,pb,n) for n in boxes):continue
            candidate=cost+math.dist(pa,pb)
            if candidate<costs.get(other,float('inf')):
                costs[other]=candidate;previous[other]=point;heapq.heappush(queue,(candidate,other))
    if target not in costs:return [a,b] # warnings expose unresolved route, never remove it.
    route=[points[target]];point=target
    while point!=source:point=previous[point];route.append(points[point])
    route.reverse();compact=[route[0]]
    for i in range(1,len(route)-1):
        p0,p1,p2=compact[-1],route[i],route[i+1]
        if (p0[0]==p1[0]==p2[0]) or (p0[1]==p1[1]==p2[1]):continue
        compact.append(p1)
    return compact+[route[-1]]


def edge_label_position(route,label):
    width=min(280,max(60,len(label)*11))
    # Prefer a long route segment; center above it so the label doesn't hide the edge.
    a,b=max(zip(route,route[1:]),key=lambda pair:math.dist(*pair))
    return (a[0]+b[0])/2,(a[1]+b[1])/2-24,width


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
        route = edge_route(edge, by_id)
        points = " ".join(f"{x:g},{y:g}" for x,y in route)
        parts.append(f'<polyline points="{points}" fill="none" '
                     'stroke="#777e87" stroke-width="2.5" marker-end="url(#arrow)"/>')
        label = str(edge.get('label', '')).strip()
        if label:
            cx, cy, label_width = edge_label_position(route, label)
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
        for row in text_layout(node):
            text_y = y + 8 + row['y']
            if row['kind'] == 'divider':
                parts.append(f'<line x1="{x+16:g}" y1="{text_y:g}" x2="{x+w-16:g}" y2="{text_y:g}" stroke="#a4a9b0"/>')
                continue
            weight = 'bold' if row['kind'] == 'heading' else 'normal'
            parts.append(f'<text x="{x+16+row["indent"]:g}" y="{text_y:g}" font-size="{row["size"]}" font-weight="{weight}" '
                         f'font-family="Arial, sans-serif" fill="#1d2227">'
                         f'{html.escape(row["text"])}</text>')
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
        route = edge_route(edge, by_id)
        pixels = [pos(point) for point in route]
        a, b = pixels[0], pixels[-1]
        draw.line(pixels, fill='#777e87', width=3)
        label = str(edge.get('label', '')).strip()
        if label:
            lx, ly, _ = edge_label_position(route, label)
            cx, cy = pos((lx, ly))
            box = draw.textbbox((cx, cy), label, font=edge_font, anchor='mm')
            draw.rounded_rectangle((box[0]-7, box[1]-4, box[2]+7, box[3]+4),
                                   radius=5, fill='#fff', outline='#ddd')
            draw.text((cx, cy), label, font=edge_font, fill='#30343a', anchor='mm')
        tail = pixels[-2]
        dx, dy = b[0]-tail[0], b[1]-tail[1]
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
        for row in text_layout(node):
            text_y = p1[1] + round((8 + row['y']) * scale)
            if row['kind'] == 'divider':
                draw.line([(p1[0]+round(16*scale), text_y), (p2[0]-round(16*scale), text_y)], fill='#a4a9b0', width=1)
                continue
            sized_font = ImageFont.truetype(str(font_path), round(row['size'] * scale)) if font_path.exists() else font
            draw.text((p1[0]+round((16+row['indent'])*scale), text_y), row['text'],
                      font=sized_font, fill='#1d2227', anchor='ls')
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
