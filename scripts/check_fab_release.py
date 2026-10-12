#!/usr/bin/env python3
"""Fab-specific coverage plus the portable release gate; no publishing."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'plugins/fab'
spec = importlib.util.spec_from_file_location('release_gate', PACKAGE / 'skills/delivery/scripts/check_release.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def coverage(plan):
    expected = {p.parent.name for p in (PACKAGE / 'skills').glob('*/SKILL.md')}
    expected |= {'wireframe.table-view', 'wireframe.canvas-preview', 'wireframe.native-canvas'}
    actual = {s['id'] for s in plan['surfaces']}
    return [f'Missing declared outcome: {sid}' for sid in sorted(expected - actual)]


if __name__ == '__main__':
    try:
        plan = json.loads((ROOT / 'docs/release-plan.json').read_text())
        version = json.loads((PACKAGE / 'plugin.json').read_text())['version']
        errors = gate.check(plan, version, gate.fingerprint(PACKAGE)) + coverage(plan)
    except (ValueError, KeyError, TypeError, AttributeError, OSError) as exc:
        errors = [f'Invalid Fab plan: {exc}']
    print(json.dumps({'eligible': not errors, 'errors': errors}, indent=2))
    raise SystemExit(bool(errors))
