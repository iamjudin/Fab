// Logic harness; not browser/rendering evidence.
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
class Element{constructor(tag){this.tag=tag;this.children=[];this.value='';this.textContent='';this.open=false;this.listeners={};}append(...x){this.children.push(...x)}replaceChildren(...x){this.children=x}focus(){}showModal(){this.open=true}close(){this.open=false}addEventListener(k,f){this.listeners[k]=f}}
const storage=new Map();const source=fs.readFileSync(__dirname+'/app.js','utf8');
function boot(){const els={};const context=vm.createContext({document:{getElementById:id=>els[id]??=new Element(id),createElement:t=>new Element(t)},localStorage:{getItem:k=>storage.get(k)??null,setItem:(k,v)=>storage.set(k,v)},crypto:require('node:crypto').webcrypto,structuredClone,window:{scrollY:120,scrollTo(){}},Date,console});vm.runInContext(source,context);return{els,run:s=>vm.runInContext(s,context)}}
let a=boot();const run=s=>a.run(s);const submit=()=>a.els.form.onsubmit({preventDefault(){}});const snapshot=()=>JSON.parse([...storage.values()][0]||'[]');
run('openForm()');a.els.name.value='Черновик';a.els.cancel.onclick();assert.equal(snapshot().length,0);
run('openForm()');a.els.name.value='   ';submit();assert.equal(snapshot().length,0);assert.match(a.els.formError.textContent,/непустое/);
a.els.name.value='Монстера';a.els.reminder.value='Проверить землю';a.els.fail.onclick();submit();assert.equal(a.els.sheet.open,true);assert.equal(a.els.name.value,'Монстера');assert.equal(a.els.reminder.value,'Проверить землю');assert.equal(snapshot().length,0);submit();assert.equal(a.els.sheet.open,false);assert.equal(snapshot().length,1);
run('openForm()');a.els.name.value='Второе';a.els.reminder.value='';submit();
run("mutate(next=>next[0].waterings.push({id:'w1',at:new Date().toISOString()}),'Полив сохранён')");assert.equal(snapshot()[0].waterings.length,1);assert.equal(snapshot()[1].waterings.length,0);
run('selected=plants[0].id;render()');assert.match(a.els.screen.children.map(x=>x.textContent).join(' '),/История/);
a.els.fail.onclick();run("mutate(next=>next[0].waterings=[],'Удалена запись')");assert.equal(snapshot()[0].waterings.length,1);run("mutate(next=>next[0].waterings=[],'Удалена запись')");assert.equal(snapshot()[0].waterings.length,0);
run('openForm(plants[0])');a.els.name.value='Не сохранять';a.els.cancel.onclick();assert.equal(snapshot()[0].name,'Монстера');
run('openForm(plants[0])');a.els.name.value='Монстера новая';a.els.reminder.value='';a.els.fail.onclick();submit();assert.equal(a.els.name.value,'Монстера новая');assert.equal(snapshot()[0].name,'Монстера');submit();assert.equal(snapshot()[0].name,'Монстера новая');assert.equal(snapshot()[0].reminder,'');
a=boot();assert.equal(run('plants[0].name'),'Монстера новая');assert.equal(run('plants.length'),2);
a.els.fail.onclick();run("mutate(next=>next[0].waterings.push({id:'failed',at:new Date().toISOString()}),'Полив')");assert.equal(snapshot()[0].waterings.length,0);
console.log('PASS: create/cancel, whitespace validation, failed create + retry, plant isolation, watering, history rendering model, failed correction + retry, edit/cancel, failed edit + retry, optional reminder, reload model, failed watering. Browser interaction NOT verified.');
