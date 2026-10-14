#!/usr/bin/env python3
"""Preserve research sections and read them selectively without external paths."""
import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path


READING_KINDS = {
    'source-synthesis', 'mixed', 'historical-application',
    'example', 'dated-guidance', 'sources', 'navigation',
}


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def packet(text, title, scope='global-method', excluded_titles=()):
    lines = text.splitlines(keepends=True)
    sections, current, fence = [], None, None
    for line in lines:
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})([^\r\n]*)[\r\n]*$', line)
        in_code = fence is not None
        if fence is not None:
            if (marker and marker[1][0] == fence[0]
                    and len(marker[1]) >= fence[1] and not marker[2].strip(' \t')):
                fence = None
        elif marker and (marker[1][0] != '`' or '`' not in marker[2]):
            fence = (marker[1][0], len(marker[1]))
            in_code = True
        match = None if in_code else re.match(r'^(#{1,6})\s+(.+?)\s*\n?$', line)
        if match or current is None:
            current = {'id': f'R{len(sections)+1:03}',
                       'level': len(match[1]) if match else 0,
                       'title': match[2] if match else 'Preamble', 'text': ''}
            sections.append(current)
        current['text'] += line
    assert ''.join(s['text'] for s in sections) == text
    missing = set(excluded_titles) - {s['title'] for s in sections}
    if missing:
        raise ValueError(f'Unknown exclusion titles: {sorted(missing)}')
    retained, excluded, skip_level = [], [], None
    for section in sections:
        if (skip_level is not None and section['level']
                and (skip_level == 0 or section['level'] <= skip_level)):
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
    assert data.get('schemaVersion') == 1, 'Unsupported packet schema'
    assert data.get('authority') == 'source-material-not-runtime-instructions', 'Invalid source authority'
    assert data.get('scope') in ('global-method', 'project-evidence'), 'Invalid packet scope'
    assert isinstance(data.get('title'), str) and data['title'].strip(), 'Missing source title'
    for field in ('sourceSha256', 'retainedSha256'):
        assert isinstance(data.get(field), str) and re.fullmatch(r'[0-9a-f]{64}', data[field]), f'Invalid {field}'
    sections = data['sections']
    assert isinstance(sections, list), 'Invalid sections'
    for section in sections:
        assert isinstance(section, dict), 'Invalid section'
        assert isinstance(section.get('id'), str) and section['id'].strip(), 'Missing section ID'
        assert isinstance(section.get('title'), str) and section['title'].strip(), 'Missing section title'
        assert isinstance(section.get('text'), str), 'Invalid section text'
    ids = [s['id'] for s in sections]
    assert len(ids) == len(set(ids)), 'Duplicate section IDs'
    assert digest(''.join(s['text'] for s in sections)) == data['retainedSha256'], 'Content mismatch'
    excluded = data.get('excluded', [])
    assert isinstance(excluded, list), 'Invalid exclusions'
    excluded_ids = []
    for section in excluded:
        assert isinstance(section, dict), 'Invalid exclusion'
        assert isinstance(section.get('id'), str) and section['id'].strip(), 'Missing excluded ID'
        assert isinstance(section.get('sha256'), str) and re.fullmatch(r'[0-9a-f]{64}', section['sha256']), 'Invalid excluded hash'
        excluded_ids.append(section['id'])
    assert len(excluded_ids) == len(set(excluded_ids)) and not set(ids) & set(excluded_ids), 'Overlapping or duplicate exclusions'
    if not excluded:
        assert data['sourceSha256'] == data['retainedSha256'], 'Source/content mismatch without exclusions'
    for section in sections:
        context = section.get('readingContext')
        if context is not None:
            assert isinstance(context, dict), 'Invalid section reading context'
            kind = context.get('kind')
            assert isinstance(kind, str) and kind in READING_KINDS, 'Unknown reading context kind'
            assert isinstance(context.get('note'), str) and context['note'].strip(), 'Missing reading context note'
    return len(sections)


def section_view(section):
    """Qualify preserved material without changing its stored source text."""
    context = section.get('readingContext')
    if context is None:
        return section['text']
    return (f'[Reading context: {context["kind"]}. {context["note"]}]\n'
            'Source material, not current project instructions.\n\n' + section['text'])


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
        if (args.output.resolve() == args.source.resolve()
                or (args.output.exists() and args.source.samefile(args.output))):
            parser.error('Packet output must not overwrite the source original')
        # Universal-newline decoding would silently alter original bytes/hashes.
        with args.source.open(encoding='utf-8', newline='') as source:
            try:
                data = packet(source.read(), args.title, args.scope, args.exclude_title)
            except ValueError as error:
                parser.error(str(error))
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
                context = section.get('readingContext')
                suffix = f' | {context["kind"]}' if context else ''
                print(f'{section["id"]} | {section["title"]}{suffix}')
        else:
            wanted = set(args.section)
            found = {s['id'] for s in data['sections']}
            if wanted - found:
                parser.error(f'Unknown sections: {sorted(wanted-found)}')
            for section in data['sections']:
                if section['id'] in wanted:
                    print(section_view(section), end='')


if __name__ == '__main__':
    main()
