#!/usr/bin/env python3
"""Read a compiled current view; no original-report or repository dependency."""
import argparse,hashlib,json,re
from pathlib import Path
PACKAGE=Path(__file__).resolve().parents[3]
def revision(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def checked_revision(value):return revision({k:v for k,v in value.items() if k!='revision'})
def validate_data(data):
    if not isinstance(data,dict) or data.get('schemaVersion')!=2 or data.get('revision')!=checked_revision(data):raise ValueError('invalid-compiled-view')
    if data.get('family')!='fab-knowledge' or data.get('authority')!='qualified-evidence-not-runtime-instructions':raise ValueError('invalid-view-authority')
    if not isinstance(data.get('provenance'),dict) or not isinstance(data.get('records'),list):raise ValueError('invalid-view-shape')
    units={}
    for u in data['records']:
        if u['id'] in units or u.get('revision')!=checked_revision(u):raise ValueError('duplicate-or-corrupt-unit')
        if u['status'] not in {'active','disputed','superseded'}:raise ValueError('invalid-unit-status')
        if u['status']=='superseded':
            if 'body' in u:raise ValueError('retired-body-in-current-view')
        elif u.get('authority')!='qualified-knowledge' or not isinstance(u.get('body'),str) or not u['body'].strip():raise ValueError('invalid-shared-meaning')
        for field in ['aliases','topics','triggers']:
            values=u.get(field,[])
            if not isinstance(values,list) or any(not isinstance(v,str) or not v.strip() for v in values):raise ValueError('invalid-discovery-metadata')
        for source in u['sources']:
            receipt=data['provenance'].get(source['sourceId'])
            if not receipt or receipt['textSha256']!=source['textSha256'] or not re.fullmatch('[a-f0-9]{64}',source['textSha256']):raise ValueError('invalid-source-receipt')
        units[u['id']]=u
    for u in units.values():
        for relation,targets in u['relations'].items():
            if relation not in {'contradicts','applies-under','supersedes','related-to'} or not isinstance(targets,list) or any(t not in units for t in targets):raise ValueError('invalid-relation')
    legacy=data.get('legacyStateFamilies',{})
    if not isinstance(legacy,dict) or any(not isinstance(k,str) or k==data['family'] or not isinstance(v,list) or len(v)!=len(set(v)) or any(x not in units for x in v) for k,v in legacy.items()):raise ValueError('invalid-legacy-family')
    visited=set();visiting=set()
    def visit(key):
        if key in visiting:raise ValueError('condition-cycle')
        if key in visited:return
        visiting.add(key)
        for target in units[key]['relations'].get('applies-under',[]):visit(target)
        visiting.remove(key);visited.add(key)
    for key in units:visit(key)
    return units

def load(data_path=None,state_path=None):
    path=Path(data_path) if data_path else PACKAGE/'shared/knowledge/current.json'
    if not path.resolve().is_relative_to(PACKAGE.resolve()):raise ValueError('view-outside-package')
    data=json.loads(path.read_text());units=validate_data(data);state={'retired':{},'reason':{},'observations':[]}
    if state_path:
        state=json.loads(Path(state_path).read_text())
        if not isinstance(state,dict) or set(state)-{'schemaVersion','family','retired','reason','observations'} or state.get('schemaVersion')!=2:raise ValueError('invalid-project-state')
        allowed=set(units) if state.get('family')==data['family'] else set(data.get('legacyStateFamilies',{}).get(state.get('family'),[]))
        if not allowed:raise ValueError('invalid-project-state')
        if not isinstance(state.get('retired'),dict) or not isinstance(state.get('reason',{}),dict) or not isinstance(state.get('observations',[]),list):raise ValueError('invalid-state-shape')
        for key,pin in state['retired'].items():
            if key not in allowed or pin!=units[key]['revision']:raise ValueError('stale-retirement')
        if set(state.get('reason',{}))-set(state['retired']):raise ValueError('unbound-reason')
        seen=set()
        for item in state.get('observations',[]):
            if set(item)!={'id','aboutUnit','unitRevision','text','origin'} or item['id'] in seen or item['id'] in units:raise ValueError('invalid-local-evidence')
            key=item['aboutUnit']
            if key not in allowed or item['unitRevision']!=units[key]['revision']:raise ValueError('stale-local-evidence')
            if not isinstance(item['text'],str) or not item['text'].strip() or len(item['text'])>4000 or not isinstance(item['origin'],str):raise ValueError('invalid-local-evidence-text')
            seen.add(item['id'])
    return data,units,state

def reason(key,units,state):
    if units[key]['status']=='superseded':return 'superseded-revision'
    if key in state['retired']:return 'project-retired-revision: '+state.get('reason',{}).get(key,'review-required')
    for target in units[key]['relations'].get('applies-under',[]):
        if reason(target,units,state):return 'unavailable-condition: '+target
    return None

def read_view(data_path=None,state_path=None,unit_id=None,query=None,expand_related=False):
    data,units,state=load(data_path,state_path)
    out={'datasetRevision':data['revision'],'family':data['family'],'authority':data['authority'],'units':[],'unavailable':[],'sourceReceipts':{},'projectEvidence':[],'archiveAccess':'Receipts only; originals are optional separate repository evidence, not assumed present in this runtime.'}
    if unit_id and unit_id not in units:raise ValueError('unknown-unit')
    selected=[unit_id] if unit_id else list(units)
    if query is not None:
        if unit_id:raise ValueError('query-with-unit')
        def terms_for(text):
            words=re.findall(r'[\w-]{3,}',text.casefold())
            # A bounded lexical heuristic, not a language model or complete lemmatizer.
            return {word[:-1] if re.fullmatch(r'[а-яё]{5,}[аяуюыиео]',word) else word for word in words}
        terms=terms_for(query)
        def score(u):
            values=[u['title']]+u.get('aliases',[])+u.get('topics',[])+u.get('triggers',[])
            words=terms_for(' '.join(values))
            token_score=sum(any(a==b or (len(a)>=4 and len(b)>=4 and (a.startswith(b) or b.startswith(a))) for b in words) for a in terms)
            phrase=' '.join(query.casefold().split())
            phrase_hit=len(terms)>1 and any(phrase in ' '.join(value.casefold().split()) for value in values)
            return token_score+(len(terms)+1 if phrase_hit else 0)
        ranked=sorted(((score(u),key) for key,u in units.items()),key=lambda x:(-x[0],x[1]))
        selected=[key for value,key in ranked if value>0]
        out['retrieval']='Lexical title/alias/topic/trigger matching with limited Russian ending normalization; not full lemmatization, semantic completeness or authority.'
        out['query']=query
    associations=[]
    if unit_id and not reason(unit_id,units,state):
        # Conditions and contradictions qualify the selected advice. Associations
        # are discovery leads, not prerequisites or an instruction to preload.
        pending=[unit_id];seen=set()
        while pending:
            current=pending.pop(0)
            if current in seen:continue
            seen.add(current)
            for relation in ['contradicts','applies-under']:
                for key in units[current]['relations'].get(relation,[]):
                    selected.append(key)
                    if not reason(key,units,state):pending.append(key)
            associations+=units[current]['relations'].get('related-to',[])
        associations=list(dict.fromkeys(key for key in associations if key not in selected))
        if expand_related:selected+=associations
        else:
            out['related']=[]
            for key in associations:
                u=units[key];blocked=reason(key,units,state)
                if blocked:
                    refs={s['sourceId']:data['provenance'][s['sourceId']] for s in u['sources']}
                    out['unavailable'].append({'id':key,'reason':blocked,'reviewSources':refs})
                else:out['related'].append({k:u[k] for k in ['id','title','status','authority','revision']})
            out['relatedReading']='Associations only. Read a relevant id explicitly; conditions and contradictions are included in units.'
    for key in dict.fromkeys(selected):
        u=units[key];blocked=reason(key,units,state)
        refs={s['sourceId']:data['provenance'][s['sourceId']] for s in u['sources']}
        if blocked:out['unavailable'].append({'id':key,'reason':blocked,'reviewSources':refs})
        else:
            out['units'].append(u if unit_id else {k:u[k] for k in ['id','title','status','authority','aliases','topics','triggers','revision'] if k in u})
            if unit_id:out['sourceReceipts'].update(refs)
    for item in state.get('observations',[]):
        if item['aboutUnit'] in selected:
            evidence={'id':item['id'],'aboutUnit':item['aboutUnit'],'scope':'project-only','authority':'local-evidence-not-shared-policy','origin':item['origin']}
            if unit_id:evidence['text']=item['text']
            out['projectEvidence'].append(evidence)
    return out

def main():
    ap=argparse.ArgumentParser();group=ap.add_mutually_exclusive_group(required=True);group.add_argument('--index',action='store_true');group.add_argument('--unit');group.add_argument('--query');ap.add_argument('--state',type=Path);ap.add_argument('--expand-related',action='store_true',help='Include association bodies as well as necessary conditions and contradictions');args=ap.parse_args()
    if args.expand_related and not args.unit:ap.error('--expand-related requires --unit')
    try:out=read_view(state_path=args.state,unit_id=args.unit,query=args.query,expand_related=args.expand_related)
    except (ValueError,KeyError,TypeError,OSError) as error:
        print(json.dumps({'error':str(error),'meaning':'Current view unavailable; do not silently fall back to retired examples.'}));raise SystemExit(2)
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
