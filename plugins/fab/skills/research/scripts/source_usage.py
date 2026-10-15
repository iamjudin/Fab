#!/usr/bin/env python3
"""Add project tags without renaming sources; hide legacy usage metadata at EOF."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tempfile

START = '<!-- fab-research-usage:start -->'
END = '<!-- fab-research-usage:end -->'
FOOTER = '<!-- fab-source-usage:v1'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def scalar(raw):
    raw = raw.strip()
    if raw.startswith('"'):
        try:
            return json.loads(raw)
        except ValueError as exc:
            raise ValueError('Unsupported quoted YAML tag') from exc
    if raw.startswith("'"):
        if len(raw) < 2 or not raw.endswith("'"):
            raise ValueError('Unclosed YAML tag')
        return raw[1:-1].replace("''", "'")
    if not raw or raw[0] in '!&*[{>|' or ': ' in raw:
        raise ValueError('Unsupported YAML tags value; preserve and review manually')
    return raw


def tokens(raw, delimiter=None):
    """Split flat YAML tag scalars/comments without splitting quoted commas."""
    quote = None
    escaped = False
    parts, start, i = [], 0, 0
    while i < len(raw):
        c = raw[i]
        if quote:
            if quote == '"' and c == '\\' and not escaped:
                escaped = True; i += 1; continue
            if c == quote and not escaped:
                if quote == "'" and i + 1 < len(raw) and raw[i + 1] == "'":
                    i += 2; continue
                quote = None
            escaped = False
        elif c in "\"'":
            quote = c
        elif c == '#' and (i == 0 or raw[i - 1].isspace()):
            return parts + [raw[start:i].rstrip()], raw[i:]
        elif delimiter and c == delimiter:
            parts.append(raw[start:i].strip()); start = i + 1
        i += 1
    if quote:
        raise ValueError('Unclosed YAML tags quote')
    return parts + [raw[start:].strip()], ''


def frontmatter(text):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip('\r\n') != '---':
        return [], text
    for i in range(1, len(lines)):
        if lines[i].rstrip('\r\n') == '---':
            return lines[:i + 1], ''.join(lines[i + 1:])
    raise ValueError('Unclosed frontmatter; no changes made')


def add_tags(text, wanted, nl):
    fm, body = frontmatter(text)
    if not fm:
        return '---' + nl + 'tags:' + nl + ''.join('  - ' + json.dumps(t, ensure_ascii=False) + nl for t in wanted) + '---' + nl + body
    if any(re.match(r'^\s*[\{\[]|^<<\s*:', line) for line in fm[1:-1]):
        raise ValueError('Unsupported JSON/merged frontmatter; preserve and review manually')
    hits = [i for i, line in enumerate(fm[1:-1], 1) if re.match(r"^(?:tags|\"tags\"|'tags')\s*:", line)]
    if len(hits) > 1:
        raise ValueError('Duplicate YAML tags keys; no changes made')
    if not hits:
        fm[-1:-1] = ['tags:' + nl] + ['  - ' + json.dumps(t, ensure_ascii=False) + nl for t in wanted]
        return ''.join(fm) + body
    i = hits[0]
    raw = fm[i].split(':', 1)[1].rstrip('\r\n')
    values, comment = tokens(raw)
    value = values[0].strip()
    end = i + 1
    if value.startswith('['):
        if not value.endswith(']'):
            raise ValueError('Unsupported multiline/invalid YAML tag list')
        items, inner_comment = tokens(value[1:-1], ',')
        if inner_comment:
            raise ValueError('Unsupported comment inside YAML flow tags')
        existing = [scalar(x).lstrip('#').casefold() for x in items if x]
        missing = [t for t in wanted if t.casefold() not in existing]
        if missing:
            pos = fm[i].index('[') + len(value) - 1
            addition = (' ' if value[1:-1].rstrip().endswith(',') else ', ' if items and items[0] else '') + ', '.join(json.dumps(t, ensure_ascii=False) for t in missing)
            fm[i] = fm[i][:pos] + addition + fm[i][pos:]
    elif value:
        existing = [scalar(value).lstrip('#').casefold()]
        missing = [t for t in wanted if t.casefold() not in existing]
        if missing:
            fm[i:i + 1] = ['tags:' + (' ' + comment if comment else '') + nl, '  - ' + value + nl] + ['  - ' + json.dumps(t, ensure_ascii=False) + nl for t in missing]
    else:
        existing, indent = [], '  '
        while end < len(fm) - 1:
            line = fm[end].rstrip('\r\n')
            m = re.match(r'^(\s*)-\s+(.+)$', line)
            if m:
                value_parts, _ = tokens(m[2]); existing.append(scalar(value_parts[0]).lstrip('#').casefold()); indent = m[1]
            elif line.strip() and not line.lstrip().startswith('#'):
                if line[0].isspace():
                    raise ValueError('Unsupported YAML tags structure')
                break
            end += 1
        missing = [t for t in wanted if t.casefold() not in existing]
        fm[end:end] = [indent + '- ' + json.dumps(t, ensure_ascii=False) + nl for t in missing]
    return ''.join(fm) + body


def unpack(text):
    """Recognize only unfenced, explicitly managed metadata; never prose headings."""
    lines = text.splitlines(keepends=True)
    fence = None
    spans, active, footer_at = [], None, None
    for i, line in enumerate(lines):
        stripped = line.rstrip('\r\n')
        m = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', stripped)
        if fence:
            if m and m[1][0] == fence[0] and len(m[1]) >= fence[1] and not m[2].strip():
                fence = None
            continue
        if m:
            fence = (m[1][0], len(m[1])); continue
        if stripped == START:
            if active is not None:raise ValueError('Nested legacy usage block')
            active = i
        elif stripped == END:
            if active is None:raise ValueError('Orphan legacy usage end')
            spans.append((active, i + 1)); active = None
        elif stripped == FOOTER:
            if footer_at is not None or active is not None:raise ValueError('Ambiguous usage footer')
            footer_at = i
    if active is not None:raise ValueError('Unclosed legacy usage block')
    metadata = {'schemaVersion': 1}
    if footer_at is not None:
        suffix = ''.join(lines[footer_at:])
        match = re.fullmatch(re.escape(FOOTER) + r'\r?\n(.*?)\r?\n-->(?:\r?\n)?', suffix, re.S)
        if not match or footer_at == 0:raise ValueError('Usage footer must be an EOF comment with its separator')
        metadata = json.loads(match[1])
        if not isinstance(metadata, dict) or metadata.get('schemaVersion') != 1:raise ValueError('Unsupported usage footer schema')
        prefix = ''.join(lines[:footer_at])
        separator = '\r\n' if prefix.endswith('\r\n') else '\n'
        text = prefix[:-len(separator)]
        lines = text.splitlines(keepends=True)
    legacy = [''.join(lines[a:b]) for a, b in spans]
    for a, b in reversed(spans):del lines[a:b]
    return ''.join(lines), metadata, legacy


def transform(data, project, usage_record=None):
    if not re.fullmatch(r'[a-z][a-z0-9_-]*', project):
        raise ValueError('Project must be an accepted lowercase slug, e.g. fab, ujitsu or once')
    text = data.decode('utf-8')
    bom = '\ufeff' if text.startswith('\ufeff') else ''
    text = text[len(bom):]
    nl = '\r\n' if '\r\n' in text else '\n'
    clean, metadata, legacy = unpack(text)
    _, body = frontmatter(clean)
    wanted = ['project/' + project]
    for block in legacy:
        for line in block.splitlines():
            if re.fullmatch(r'\s*#[\w/-]+(?:[ \t]+#[\w/-]+)*\s*', line):
                wanted.extend(t[1:] for t in line.split())
        content = block.split(START, 1)[1].rsplit(END, 1)[0].strip()
        if content.startswith('{'):
            old = json.loads(content)
            for row in old.get('projects', []):
                if isinstance(row, dict) and isinstance(row.get('tag'), str):wanted.append(row['tag'].lstrip('#'))
    wanted = list(dict.fromkeys(wanted))
    tagged = add_tags(clean, wanted, nl)
    assert frontmatter(tagged)[1] == body, 'Reader body changed'
    if legacy:
        rows = metadata.setdefault('legacy', [])
        if not isinstance(rows, list):raise ValueError('Invalid legacy provenance list')
        rows.extend({'format':'fab-research-usage', 'text':s} for s in legacy)
    if usage_record is not None:
        if not isinstance(usage_record, dict):raise ValueError('Usage record must be a JSON object')
        if usage_record.get('project') != project:raise ValueError('Usage record project mismatch')
        if 'bodySha256' in usage_record and usage_record['bodySha256'] != digest(body.encode('utf-8')):raise ValueError('Usage revision does not match source body')
        if usage_record.get('processedAt'):datetime.date.fromisoformat(usage_record['processedAt'])
        rows = metadata.setdefault('projects', [])
        if not isinstance(rows, list):raise ValueError('Invalid footer projects')
        matches = [i for i, row in enumerate(rows) if isinstance(row, dict) and row.get('project') == project]
        if len(matches)>1:raise ValueError('Duplicate project records require review')
        if matches:rows[matches[0]] = usage_record
        else:rows.append(usage_record)
    result = tagged
    if legacy or usage_record is not None or metadata != {'schemaVersion':1}:
        payload = json.dumps(metadata, ensure_ascii=False, indent=2).replace('<','\\u003c').replace('>','\\u003e')
        result += nl + FOOTER + nl + payload.replace('\n', nl) + nl + '-->' + nl
    return (bom + result).encode('utf-8'), {'tag':'project/' + project,'preservedLegacyBlocks':len(legacy),'bodySha256':digest(body.encode('utf-8')),'renamed':False}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source', type=Path);ap.add_argument('--project',required=True)
    ap.add_argument('--record',type=Path,help='Optional actual project provenance JSON; layout migration alone must not invent one')
    ap.add_argument('--apply',action='store_true');ap.add_argument('--expected-sha')
    args=ap.parse_args();temp=None
    try:
        if args.source.is_symlink() or args.source.stat().st_nlink != 1:raise ValueError('Refuse symlink/hardlinked source')
        before=args.source.read_bytes();info=args.source.stat()
        if args.expected_sha and digest(before)!=args.expected_sha:raise ValueError('Source changed since review')
        record=json.loads(args.record.read_text()) if args.record else None
        result,receipt=transform(before,args.project,record)
        if args.apply and not args.expected_sha:raise ValueError('--apply requires reviewed --expected-sha')
        if args.apply and result!=before:
            with tempfile.NamedTemporaryFile(dir=args.source.parent,prefix='.fab-tag-',delete=False) as f:
                temp=Path(f.name);f.write(result)
            os.chmod(temp,stat.S_IMODE(info.st_mode))
            if args.source.read_bytes()!=before or args.source.stat().st_ino!=info.st_ino:raise ValueError('Concurrent source change; no replacement')
            os.replace(temp,args.source);temp=None
        print(json.dumps({**receipt,'changed':result!=before,'applied':args.apply,'beforeSha256':digest(before),'afterSha256':digest(result)}))
    except (OSError,ValueError,KeyError,TypeError,AssertionError) as exc:
        print(json.dumps({'error':str(exc),'applied':False}));return 1
    finally:
        if temp is not None:temp.unlink(missing_ok=True)
    return 0


if __name__=='__main__':raise SystemExit(main())
