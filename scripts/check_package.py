#!/usr/bin/env python3
"""Validate package references, methods and optional installed parity."""
import argparse, hashlib, importlib.util, json, re, struct, zlib
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1] / 'plugins/fab'
reader_spec = importlib.util.spec_from_file_location(
    'fab_research_reader', ROOT / 'skills/research/scripts/research_packet.py')
reader = importlib.util.module_from_spec(reader_spec)
reader_spec.loader.exec_module(reader)
def payload(root):
    return {str(p.relative_to(root)):p.read_bytes() for p in root.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith('.pyc')}
def fingerprint(files):
    h=hashlib.sha256()
    for name,content in sorted(files.items()):
        h.update(name.encode()+b'\0');h.update(hashlib.sha256(content).digest())
    return h.hexdigest()[:16]
def validate_branding(root, manifest):
    """Fab's PNG distribution profile; container checks, not host rendering."""
    interface = manifest['extensions']['com.openai']['interface']
    for key, limit in [('displayName', 30), ('shortDescription', 30),
                       ('longDescription', 4000), ('developerName', 80)]:
        value = interface.get(key)
        assert isinstance(value, str) and value.strip() and len(value) <= limit, key
        assert not re.search(r'[\u0400-\u04ff]', value), (key, 'English listing required')
    for key in ('composerIcon', 'logo'):
        value = interface.get(key)
        assert isinstance(value, str) and value.startswith('./'), (key, 'missing relative asset')
        path = (root / value).resolve()
        assert path.is_relative_to(root.resolve()), (key, 'asset escapes package')
        assert path.is_file() and path.suffix.lower() == '.png', (key, 'Fab requires a PNG asset')
        data = path.read_bytes()
        assert len(data) <= 5 * 1024 * 1024 and data[:8] == b'\x89PNG\r\n\x1a\n', key
        assert data[12:16] == b'IHDR' and len(data) >= 33, key
        width, height = struct.unpack('>II', data[16:24])
        assert width == height and 48 <= width <= 4096, (key, 'icon dimensions')
        offset, chunks = 8, []
        while offset < len(data):
            assert offset + 12 <= len(data), (key, 'truncated PNG')
            size = struct.unpack('>I', data[offset:offset + 4])[0]
            end = offset + 12 + size
            assert end <= len(data), (key, 'truncated PNG chunk')
            kind = data[offset + 4:offset + 8]
            chunk = data[offset + 4:offset + 8 + size]
            crc = struct.unpack('>I', data[offset + 8 + size:end])[0]
            assert zlib.crc32(chunk) & 0xffffffff == crc, (key, 'PNG CRC mismatch')
            chunks.append(kind)
            offset = end
        assert chunks[0] == b'IHDR' and b'IDAT' in chunks and chunks[-1] == b'IEND', key

def validate_methods(root):
    """Verify the registry against actual pairs, not just self-consistent packets."""
    methods = root / 'shared/methods'
    registry = json.loads((methods / 'registry.json').read_text())
    assert registry.get('schemaVersion') == 1, 'Unsupported method registry'
    modules = registry.get('modules')
    assert isinstance(modules, list), 'Missing method modules'
    ids, pairs = set(), {'brief': set(), 'full': set()}
    for module in modules:
        module_id = module.get('id')
        assert isinstance(module_id, str) and module_id.strip() and module_id not in ids, 'Duplicate/missing method ID'
        ids.add(module_id)
        paths = {}
        for field, suffix in [('brief', '.md'), ('full', '.full.json')]:
            value = module.get(field)
            assert isinstance(value, str) and value.strip(), (module_id, field, 'missing path')
            path = (methods / value).resolve()
            assert path.is_relative_to(methods.resolve()) and path.is_file(), (module_id, field, 'invalid path')
            assert path.name.endswith(suffix) and path not in pairs[field], (module_id, field, 'invalid/duplicate pair')
            pairs[field].add(path)
            paths[field] = path
        data = json.loads(paths['full'].read_text())
        reader.validate(data)
        assert data['scope'] == 'global-method', (module_id, 'wrong bundled scope')
        assert module.get('sourceSha256') == data['sourceSha256'], (module_id, 'registry source mismatch')
        assert module.get('sourceTitle') == data['title'], (module_id, 'registry title mismatch')
        links = re.findall(r'\]\(([^)]+)\)', paths['brief'].read_text())
        assert paths['full'] in {(paths['brief'].parent / t.split('#')[0]).resolve()
                                 for t in links if '://' not in t}, (module_id, 'brief does not link its packet')
        # A preserved source or another brief is not the executable policy owner.
        brief_text = paths['brief'].read_text()
        application = re.search(r'^## Application in current Fab\s*\n(.*?)(?=^## |\Z)',
                                brief_text, re.M | re.S)
        assert application is not None, (module_id, 'missing current application boundary')
        owner_links = []
        for target in re.findall(r'\]\(([^)]+)\)', application.group(1)):
            if '://' in target or target.startswith('#'):
                continue
            owner = (paths['brief'].parent / target.split('#')[0]).resolve()
            if (owner.is_relative_to(root.resolve()) and not owner.is_relative_to(methods.resolve())
                    and owner.is_file() and owner.suffix == '.md'):
                owner_links.append(owner)
        assert owner_links, (module_id, 'missing current policy owner link')
        context = module.get('readingContext')
        if context is not None:
            counts = dict(Counter(s['readingContext']['kind'] for s in data['sections'] if s.get('readingContext') is not None))
            assert isinstance(context, dict) and context.get('sectionKinds') == counts, (module_id, 'registry context drift')
            assert isinstance(context.get('boundary'), str) and context['boundary'].strip(), (module_id, 'missing context boundary')
    actual = {p.resolve() for p in methods.rglob('*.full.json')}
    assert pairs['full'] == actual, 'Unregistered method packet'
    table_links, in_table = set(), False
    for line in (methods / 'index.md').read_text().splitlines():
        if re.fullmatch(r'\|(?:\s*:?-+:?\s*\|)+\s*', line):
            in_table = True
        elif not line.startswith('|'):
            in_table = False
        elif in_table:
            table_links.update((methods / target.split('#')[0]).resolve()
                               for target in re.findall(r'\]\(([^)]+)\)', line)
                               if '://' not in target)
    assert pairs['brief'] <= table_links, 'Method missing from the index decision table'

def validate(root):
    manifest=json.loads((root/'plugin.json').read_text())
    assert manifest['name']=='fab'
    validate_branding(root, manifest)
    for p in root.rglob('*.md'):
        text=p.read_text();assert text.count('```')%2==0,p
        # Prompt format contains a literal Markdown link example, not a resource.
        if p.name=='deep-research.md':continue
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in target or target.startswith('#'):continue
            q=(p.parent/target.split('#')[0]).resolve()
            assert q.is_relative_to(root.resolve()), (p,target,'outside package')
            assert q.exists(), (p,target,'missing')
    for p in (root/'skills').glob('*/SKILL.md'):
        head=p.read_text().split('---',2)[1]
        assert f'name: {p.parent.name}\n' in head
        assert 'description: ' in head
    validate_methods(root)
    return manifest
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--installed-root',type=Path);args=parser.parse_args()
    m=validate(ROOT); files=payload(ROOT)
    if args.installed_root:
        other=payload(args.installed_root)
        differences=[p for p in sorted(files.keys()|other.keys()) if files.get(p)!=other.get(p)]
        assert not differences, differences
    print(f"PASS: {m['version']}; {len(files)} files; fingerprint={fingerprint(files)}")
