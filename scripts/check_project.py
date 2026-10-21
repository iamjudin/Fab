#!/usr/bin/env python3
"""Check maintained documentation and explicit task leftovers; never delete files."""
import argparse
import json
import os
from pathlib import Path
import posixpath
import re
import subprocess
import unicodedata
from urllib.parse import unquote, urlsplit

CURRENT_DOCS = (
    'README.md', 'docs/backlog.md', 'docs/limitations.md', 'docs/development.md',
    'docs/install.md', 'docs/architecture/design.md', 'docs/handoff.md',
)


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True)


def prose(text):
    """Fenced examples are text, not promised downloadable resources."""
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            lines.append('')
        elif fence is None:
            lines.append(line)
    return '\n'.join(lines)


def anchors(text):
    text = prose(text)
    result = set(re.findall(r'<a\s+id=["\']([^"\']+)', text))
    counts = {}
    for line in text.splitlines():
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if not match:
            continue
        heading = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', match.group(1))
        heading = re.sub(r'<[^>]*>', '', heading).lower()
        slug = ''.join(c for c in heading if c in ' _-'
                       or unicodedata.category(c)[0] in 'LNM').replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug + (f'-{count}' if count else ''))
    return result


def check(root, staged=False, base_ref=None, task_dirs=()):
    root = Path(root).resolve()
    tracked = set(git(root, 'ls-files', '-z').split('\0')) - {''}
    symlinks = {row.split('\t', 1)[1] for row in git(root, 'ls-files', '--stage', '-z').split('\0')
                if row.startswith('120000 ')}
    errors, checked = [], 0

    def read(path):
        if staged:
            return git(root, 'show', ':' + path)
        return (root / path).read_text()

    if staged:
        changed = git(root, 'diff', '--cached', '--name-only', '--diff-filter=ACMR', '-z')
    elif base_ref and set(base_ref) != {'0'}:
        # Resolve to an object first; a ref is never interpolated into shell code.
        base = git(root, 'rev-parse', '--verify', base_ref + '^{commit}').strip()
        changed = git(root, 'diff', '--name-only', '--diff-filter=ACMR', '-z', base, 'HEAD')
    else:
        changed = git(root, 'diff', '--name-only', '--diff-filter=ACMR', '-z', 'HEAD')
    changed = set(changed.split('\0')) - {''}
    selected = (set(CURRENT_DOCS) & tracked) | {p for p in changed if p.endswith('.md')}

    for source in sorted(selected & tracked):
        if source in symlinks:
            errors.append(f'{source}: maintained document must be a regular Git file')
            continue
        try:
            text = prose(read(source))
        except (OSError, subprocess.CalledProcessError) as exc:
            errors.append(f'{source}: cannot read selected document: {type(exc).__name__}')
            continue
        targets = re.findall(r'\[[^\]\n]*\]\((<[^>]+>|[^)\n]+)\)', text)
        targets += re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)', text)
        for target in targets:
            target = target.strip('<>')
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            path = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(url.path))) if url.path else source
            if url.path.startswith('/') or path == '..' or path.startswith('../'):
                errors.append(f'{source}: link leaves repository: {target}')
                continue
            # Existence on the maintainer's disk is insufficient for publication.
            if path not in tracked:
                errors.append(f'{source}: target is not in the Git index: {target}')
                continue
            if path in symlinks or (not staged and not (root / path).resolve().is_relative_to(root)):
                errors.append(f'{source}: target must be a regular repository file: {target}')
                continue
            try:
                target_text = read(path) if path.endswith('.md') else None
                if not staged and not (root / path).is_file():
                    raise FileNotFoundError(path)
                if url.fragment and target_text is not None and unquote(url.fragment) not in anchors(target_text):
                    errors.append(f'{source}: missing heading/anchor: {target}')
            except (OSError, subprocess.CalledProcessError) as exc:
                errors.append(f'{source}: unavailable target {target}: {type(exc).__name__}')
            checked += 1

    manifest_path = 'plugins/fab/plugin.json'
    if manifest_path in tracked:
        try:
            version = json.loads(read(manifest_path))['version']
            for source in ('README.md', 'docs/install.md'):
                if source not in tracked:
                    continue
                pins = re.findall(r'--ref\s+v(\d+\.\d+\.\d+(?:-[\w.]+)?)', read(source))
                if not pins or any(pin != version for pin in pins):
                    errors.append(f'{source}: installation pin must match source package {version}')
        except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
            errors.append(f'Invalid version source: {type(exc).__name__}')

    task_leftovers = []
    for directory in task_dirs:
        path = Path(directory)
        if path.is_absolute() or '..' in path.parts or not path.parts or path == Path('.'):
            errors.append(f'Task boundary must be a specific repository-relative directory: {directory}')
            continue
        if not (root / path).resolve().is_relative_to(root):
            errors.append(f'Task boundary leaves repository: {directory}')
            continue
        # Only caller-owned roots are examined. Other pending work is not a defect.
        found = git(root, 'ls-files', '--others', '--exclude-standard', '-z', '--', str(path))
        task_leftovers.extend(p for p in found.split('\0') if p)
    for path in sorted(set(task_leftovers)):
        errors.append(f'Task file needs a disposition (stage, retain privately or remove): {path}')
    return {'eligible': not errors, 'documents': len(selected & tracked),
            'localLinks': checked, 'taskRoots': list(task_dirs), 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--staged', action='store_true', help='Read the prospective commit, not unstaged edits')
    parser.add_argument('--base-ref', default=os.environ.get('FAB_CHECK_BASE') or None,
                        help='Check changed Markdown since this commit, plus current entry documents')
    parser.add_argument('--task-dir', action='append', default=[],
                        help='Explicitly owned directory to check for untracked non-private files')
    args = parser.parse_args()
    try:
        result = check(args.root, args.staged, args.base_ref, args.task_dir)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        result = {'eligible': False, 'errors': [f'Project check failed: {type(exc).__name__}: {exc}']}
    print(json.dumps(result, indent=2))
    return int(not result['eligible'])


if __name__ == '__main__':
    raise SystemExit(main())
