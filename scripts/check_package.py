#!/usr/bin/env python3
"""Validate package references, methods and optional installed parity."""
import argparse, hashlib, importlib.util, json, re, struct, zlib
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
    for p in (root/'shared/methods').glob('*.full.json'):
        d=json.loads(p.read_text());assert d['scope']=='global-method'
        reader.validate(d)
        content=''.join(s['text'] for s in d['sections'])
        assert hashlib.sha256(content.encode()).hexdigest()==d['retainedSha256']
    return manifest
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--installed-root',type=Path);args=parser.parse_args()
    m=validate(ROOT); files=payload(ROOT)
    if args.installed_root:
        other=payload(args.installed_root)
        differences=[p for p in sorted(files.keys()|other.keys()) if files.get(p)!=other.get(p)]
        assert not differences, differences
    print(f"PASS: {m['version']}; {len(files)} files; fingerprint={fingerprint(files)}")
