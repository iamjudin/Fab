"""Read-only helper probe using synthetic data, never a vault handoff."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
helper = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location('bookworm_probe', helper)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
example = Path(__file__).with_name('reading-example.md').read_text()
paragraph = example.split('## Before\n\n', 1)[1].split('\n\n## After', 1)[0]
source = '## Pilot\n\n' + paragraph + '\n'
result = module.refine_markdown(source, toc_title='Contents')
compact = module.refine_markdown('## Modes\n\n**Guided:** Required fields\n\n**Free:** Unrestricted text\n', toc_title='Contents')
assert paragraph in result
assert '| Parameter | Description |' in compact
print(json.dumps({
    'helper_sha256': hashlib.sha256(helper.read_bytes()).hexdigest(),
    'synthetic_input_sha256': hashlib.sha256(source.encode()).hexdigest(),
    'dense_paragraph_preserved_verbatim': paragraph in result,
    'compact_label_fields_become_table': '| Parameter | Description |' in compact,
    'scope': 'Direct helper calls only, no model turn, source edits or vault transfer',
}, indent=2))
