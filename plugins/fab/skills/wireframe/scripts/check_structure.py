#!/usr/bin/env python3
"""Physical ownership guard for a Canvas structure overview, not flow-only maps."""
import argparse,json,re
from pathlib import Path

def contains(a,b):
    return a.get('type')=='group' and all((float(a['x'])<=float(b['x']),float(a['y'])<=float(b['y']),float(a['x'])+float(a['width'])>=float(b['x'])+float(b['width']),float(a['y'])+float(a['height'])>=float(b['y'])+float(b['height'])))

def check(canvas,surface_ids):
    nodes=canvas.get('nodes',[]);by_id={n['id']:n for n in nodes};errors=[];frames={}
    for sid in surface_ids:
        found=[n for n in nodes if n.get('type')=='group' and (n['id']==sid or re.match(re.escape(sid)+r'\b',str(n.get('label',''))))]
        if len(found)!=1:
            errors.append(f'{sid}: expected one real surface group, found {len(found)}');continue
        frames[sid]=found[0]
        if not any(n['id']!=found[0]['id'] and n.get('type')!='group' and contains(found[0],n) for n in nodes):
            errors.append(f'{sid}: empty surface group has no owned content')
    global_navigation=[n for n in nodes if n.get('type')=='group' and n['id'].startswith('global-navigation')]
    owners=list(frames.values())+global_navigation
    for edge in canvas.get('edges',[]):
        source=by_id.get(edge.get('fromNode'))
        if not source:errors.append(f'{edge.get("id")}: missing source');continue
        if source.get('type')=='file' or edge.get('relation')=='documentation':continue
        if source.get('type')=='group':
            errors.append(f'{edge.get("id")}: navigation must originate at a control, not anonymous group');continue
        if not any(contains(frame,source) for frame in owners):
            errors.append(f'{edge.get("id")}: navigation source {source["id"]} has no physical surface owner')
    return errors

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('canvas',type=Path);p.add_argument('--surface-id',action='append',required=True);a=p.parse_args()
    errors=check(json.loads(a.canvas.read_text()),a.surface_id)
    print('\n'.join(errors) if errors else 'PASS: declared surfaces/control sources have physical containment')
    print('Boundary: does not prove correct semantic ownership, nesting depth, colour or native rendering.')
    raise SystemExit(bool(errors))
