#!/usr/bin/env python3
"""Preserve research sections and read them selectively without external paths."""
import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def packet(text, title, scope='global-method', excluded_titles=()):
    lines = text.splitlines(keepends=True)
    sections, current, fence = [], None, False
    for line in lines:
        if line.lstrip().startswith(('```', '~~~')):
            fence = not fence
        match = None if fence else re.match(r'^(#{1,6})\s+(.+?)\s*\n?$', line)
        if match or current is None:
            current = {'id': f'R{len(sections)+1:03}',
                       'level': len(match[1]) if match else 0,
                       'title': match[2] if match else 'Preamble', 'text': ''}
            sections.append(current)
        current['text'] += line
    assert ''.join(s['text'] for s in sections) == text
    retained, excluded, skip_level = [], [], None
    for section in sections:
        if skip_level is not None and section['level'] and section['level'] <= skip_level:
            skip_level = None
        if section['title'] in excluded_titles:
            skip_level = section['level']
        (excluded if skip_level is not None else retained).append(section)
    return {'schemaVersion': 1, 'scope': scope, 'title': title,
            'sourceSha256': digest(text), 'sourceDate': None,
            'ingestedAt': date.today().isoformat(),
            'authority': 'source-material-not-runtime-instructions',
            'validation': {'structure': 'lossless sections; explicit exclusions',
                           'claims': 'not exhaustively fact-checked'},
            'retainedSha256': digest(''.join(s['text'] for s in retained)),
            'excluded': [{'id': s['id'], 'title': s['title'],
                          'sha256': digest(s['text']), 'reason': 'project-specific section'}
                         for s in excluded], 'sections': retained}


def validate(data):
    sections = data['sections']
    ids = [s['id'] for s in sections]
    assert len(ids) == len(set(ids)), 'Duplicate section IDs'
    assert digest(''.join(s['text'] for s in sections)) == data['retainedSha256'], 'Content mismatch'
    assert data['scope'] in ('global-method', 'project-evidence')
    return len(sections)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    build = sub.add_parser('build')
    build.add_argument('source', type=Path)
    build.add_argument('output', type=Path)
    build.add_argument('--title', required=True)
    build.add_argument('--scope', choices=['global-method', 'project-evidence'], default='project-evidence')
    build.add_argument('--exclude-title', action='append', default=[])
    for action in ('read', 'validate'):
        cmd = sub.add_parser(action)
        cmd.add_argument('packet', type=Path)
        if action == 'read':
            choice = cmd.add_mutually_exclusive_group(required=True)
            choice.add_argument('--index', action='store_true')
            choice.add_argument('--section', action='append')
    args = parser.parse_args()
    if args.command == 'build':
        data = packet(args.source.read_text(encoding='utf-8'), args.title, args.scope, args.exclude_title)
        validate(data)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        print(f'Preserved {len(data["sections"])} sections; excluded {len(data["excluded"])}')
    else:
        data = json.loads(args.packet.read_text(encoding='utf-8'))
        count = validate(data)
        if args.command == 'validate':
            print(f'Packet structure: OK ({count} sections); claim verification separate')
        elif args.index:
            print(json.dumps({k:v for k,v in data.items() if k != 'sections'}, ensure_ascii=False, indent=2))
            for section in data['sections']:
                print(f'{section["id"]} | {section["title"]}')
        else:
            wanted = set(args.section)
            found = {s['id'] for s in data['sections']}
            if wanted - found:
                parser.error(f'Unknown sections: {sorted(wanted-found)}')
            for section in data['sections']:
                if section['id'] in wanted:
                    print(section['text'], end='')


if __name__ == '__main__':
    main()
