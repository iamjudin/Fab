#!/usr/bin/env python3
"""Fail-closed release eligibility for a declared, exact package and scope."""
import argparse
import hashlib
import json
from pathlib import Path


def fingerprint(root):
    digest = hashlib.sha256()
    for p in sorted(root.rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts or p.name.endswith('.pyc'):
            continue
        digest.update(str(p.relative_to(root)).encode() + b'\0')
        digest.update(hashlib.sha256(p.read_bytes()).digest())
    return digest.hexdigest()[:16]


def check(plan, version, package_fingerprint):
    def text(value):
        return isinstance(value, str) and bool(value.strip())

    errors = []
    if plan.get('schema') != 1:
        errors.append('Unsupported plan schema')
    if plan.get('version') != version or plan.get('fingerprint') != package_fingerprint:
        errors.append('Plan does not match exact package version/fingerprint')
    if plan.get('channel') not in ('beta', 'stable'):
        errors.append('Unknown channel')
    surfaces = plan.get('surfaces', [])
    if not surfaces or not isinstance(surfaces, list):
        return errors + ['Nonempty surface registry required']
    seen, enabled = set(), 0
    for surface in surfaces:
        sid = surface.get('id')
        if not text(sid) or sid in seen:
            errors.append('Missing/duplicate surface ID')
            continue
        seen.add(sid)
        state = surface.get('status')
        if state not in ('verified', 'limited', 'experimental', 'blocked', 'unknown'):
            errors.append(f'{sid}: unknown readiness status')
        if type(surface.get('default')) is not bool:
            errors.append(f'{sid}: explicit default boolean required')
        if surface.get('default') is not True:
            if not text(surface.get('limitations')):
                errors.append(f'{sid}: excluded/opt-in surface needs disclosure')
            continue
        enabled += 1
        if state not in ('verified', 'limited'):
            errors.append(f'{sid}: {state} cannot be enabled by default')
        if state == 'limited' and (plan.get('channel') != 'beta' or not text(surface.get('limitations'))):
            errors.append(f'{sid}: limited outcome requires beta and disclosed bounds')
        checks = surface.get('checks', [])
        if not isinstance(checks, list) or not checks:
            errors.append(f'{sid}: required checks missing')
            continue
        for result in checks:
            if not text(result.get('name')) or result.get('result') != 'pass' or not text(result.get('evidence')):
                errors.append(f'{sid}: required check failed, unknown or without evidence')
    if not enabled:
        errors.append('No default outcome included')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan', type=Path)
    parser.add_argument('--package-root', type=Path, required=True)
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text())
        manifest = json.loads((args.package_root / 'plugin.json').read_text())
        errors = check(plan, manifest['version'], fingerprint(args.package_root))
    except (ValueError, KeyError, TypeError, AttributeError, OSError) as exc:
        errors = [f'Invalid plan/package: {exc}']
    print(json.dumps({'eligible': not errors, 'errors': errors}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(errors))
