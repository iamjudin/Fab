// Application integration checks using a minimal DOM adapter; not browser/UI evidence.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync('prototype/app.js','utf8');
function harness(initial=null){
 const elements=new Map(),memory=new Map(initial===null?[]:[['community-setup-v1',initial]]);
 const element=id=>{if(!elements.has(id))elements.set(id,{id,innerHTML:'',textContent:'',value:'',checked:false,open:false,attrs:{},events:{},addEventListener(name,cb){this.events[name]=cb},setAttribute(k,v){this.attrs[k]=v},focus(){this.focused=true},showModal(){this.open=true},close(){this.open=false}});return elements.get(id)};
 const c=vm.createContext({console,structuredClone,Date,Error,Object,String,Set,Array,JSON,crypto:require('node:crypto').webcrypto,document:{querySelector:id=>['#action-error','#form-error','#title','#instructions','#assignee'].includes(id)&&!element('#sheet-body').innerHTML.includes('id="'+id.slice(1)+'"')?null:element(id)},localStorage:{getItem:k=>memory.get(k)??null,setItem:(k,v)=>memory.set(k,v)},window:{confirm:()=>true},FormData:class{constructor(form){this.data=form.data}get(k){return this.data[k]}}});
 vm.runInContext(source,c);
 return {e:element,memory,run:s=>vm.runInContext(s,c),submit(fields){element('#sheet-body').events.submit({target:{id:'task-form',data:fields},preventDefault(){}})},action(name){element('#sheet-body').events.click({target:{closest:()=>({dataset:{action:name}})}})}}
}
let h=harness();
const state=()=>JSON.parse(h.run('JSON.stringify(data)'));
const task=id=>state().tasks.find(t=>t.id===id);
h.run('form()');h.submit({title:'  ',instructions:'',assignee:'anna'});assert.match(h.e('#form-error').textContent,/Заполни/);assert.equal(state().tasks.length,4);assert.equal(h.memory.size,0);
h.run('back()');assert.equal(h.e('#sheet').open,false);assert.equal(state().tasks.length,4);
h.run('form()');h.e('#fail').checked=true;h.submit({title:'Проверить свет',instructions:'Включи свет у сцены.',assignee:'anna'});assert.equal(state().tasks.length,4);assert.match(h.e('#form-error').textContent,/отказ/);assert.equal(h.e('#sheet').open,true);
h.submit({title:'Проверить свет',instructions:'Включи свет у сцены.',assignee:'anna'});assert.equal(state().tasks.length,5);assert.equal(h.e('#sheet').open,false);assert.match(h.e('#notice').textContent,/Сохранено/);
h.run("role='volunteer';who='anna';filter='active';render()");assert.match(h.e('#tasks').innerHTML,/Расставить/);assert.doesNotMatch(h.e('#tasks').innerHTML,/Принести материалы|Разместить указатели|Подготовить стол/);
h.run("detail('materials')");assert.equal(h.e('#sheet').open,false);
h.run("detail('chairs')");h.action('toggle');assert.equal(task('chairs').completed,true);assert.match(h.e('#sheet-body').innerHTML,/Вернуть в работу/);assert.match(h.e('#sheet-body').innerHTML,/В работе → Готово/);
h.run("filter='done';render()");assert.match(h.e('#tasks').innerHTML,/Расставить/);h.action('toggle');assert.equal(task('chairs').completed,false);assert.match(h.e('#sheet-body').innerHTML,/Готово → В работе/);
h.e('#fail').checked=true;h.action('toggle');assert.equal(task('chairs').completed,false);assert.match(h.e('#action-error').textContent,/отказ/);h.e('#fail').checked=false;
h.run("role='coordinator';filter='active';render();detail('chairs');form('chairs')");h.submit({title:task('chairs').title,instructions:task('chairs').instructions,assignee:'boris'});assert.equal(task('chairs').assignee,'boris');assert.match(h.e('#sheet-body').innerHTML,/Ответственный: Анна → Борис/);
h.run("form('chairs');back()");assert.equal(task('chairs').assignee,'boris');assert.equal(h.run('view.type'),'detail');
h.action('toggle');assert.equal(task('chairs').completed,true);
h.action('cancel-task');h.action('back');assert.equal(task('chairs').cancelled,false);assert.equal(h.run('view.type'),'detail');
h.action('cancel-task');h.action('confirm-cancel');assert.equal(task('chairs').cancelled,true);assert.equal(task('chairs').completed,true);assert.match(h.e('#sheet-body').innerHTML,/Сохранённая готовность/);assert.doesNotMatch(h.e('#sheet-body').innerHTML,/data-action="toggle"/);
h.action('restore');assert.equal(task('chairs').cancelled,false);assert.equal(task('chairs').completed,true);
h.run("role='volunteer';who='vera';filter='active';render()");assert.match(h.e('#tasks').innerHTML,/пока нет/);
const stored=h.memory.get('community-setup-v1');const again=harness(stored);assert.equal(again.run("data.tasks.find(t=>t.id==='chairs').assignee"),'boris');assert.equal(again.run("data.tasks.find(t=>t.id==='chairs').completed"),true);assert.equal(again.run("data.tasks.find(t=>t.id==='chairs').history.length"),6);
again.run("form('materials')");again.submit({title:'Принести материалы для мастерской',instructions:'Уточнённая инструкция',assignee:'anna'});assert.equal(again.run("data.tasks.find(t=>t.id==='materials').completed"),true);assert.equal(again.run("data.tasks.find(t=>t.id==='materials').assignee"),'anna');again.run("form('materials')");again.submit({title:'Принести материалы для мастерской',instructions:'Уточнённая инструкция',assignee:''});assert.equal(again.run("data.tasks.find(t=>t.id==='materials').completed"),true);assert.equal(again.run("data.tasks.find(t=>t.id==='materials').assignee"),'');
h=harness('{broken');assert.equal(h.run('blocked'),true);assert.equal(h.memory.get('community-setup-v1'),'{broken');assert.match(h.e('#fatal').textContent,/заблокированы/);
h.e('#reset').onclick();assert.equal(h.run('blocked'),false);assert.equal(state().tasks.length,4);
h.run('data.tasks=[];render()');assert.match(h.e('#overview').innerHTML,/Нет активных задач/);
h.run('form()');const long='Оченьдлинноеслово'.repeat(50)+' <img src=x onerror=alert(1)>';h.submit({title:long,instructions:'Инструкция\n'.repeat(100),assignee:''});assert.equal(state().tasks[0].title,long);assert.match(h.e('#tasks').innerHTML,/&lt;img/);assert.doesNotMatch(h.e('#tasks').innerHTML,/<img src/);
// Focused recovery regression: no background control change between submit attempts.
{
 const recovery=harness();
 recovery.run("detail('materials');form('materials')");
 const before=recovery.run('JSON.stringify(data)'),markup=recovery.e('#sheet-body').innerHTML;
 const draft={title:'Материалы к вечеру',instructions:'Разложить бумагу на столах.',assignee:'anna'};
 recovery.e('#title').value=draft.title;
 recovery.e('#instructions').value=draft.instructions;
 recovery.e('#assignee').value=draft.assignee;
 recovery.e('#fail').checked=true;
 recovery.submit(draft);
 assert.equal(recovery.e('#fail').checked,false);
 assert.equal(recovery.e('#sheet').open,true);
 assert.equal(recovery.run('view.type'),'form');
 assert.equal(recovery.run('JSON.stringify(data)'),before);
 assert.equal(recovery.memory.size,0);
 assert.equal(recovery.e('#sheet-body').innerHTML,markup);
 for(const field of ['title','instructions','assignee'])assert.equal(recovery.e('#'+field).value,draft[field]);
 assert.match(recovery.e('#form-error').textContent,/Имитация снята/);
 recovery.submit(Object.fromEntries(['title','instructions','assignee'].map(field=>[field,recovery.e('#'+field).value])));
 const saved=JSON.parse(recovery.memory.get('community-setup-v1')).tasks.find(t=>t.id==='materials');
 assert.equal(saved.title,draft.title);assert.equal(saved.instructions,draft.instructions);assert.equal(saved.assignee,draft.assignee);
 assert.equal(saved.completed,true);assert.equal(saved.cancelled,false);assert.equal(saved.history.length,1);
 assert.equal(recovery.run('view.type'),'detail');assert.equal(recovery.e('#sheet').open,true);
 assert.match(recovery.e('#notice').textContent,/Сохранено/);
 assert.match(recovery.e('#sheet-body').innerHTML,/Материалы к вечеру/);
 console.log('PASS: focused one-shot edit recovery, retained draft, unchanged failed state, retry without background toggle, one saved history entry and preserved readiness (DOM adapter only).');
}
console.log('PASS: validation/cancel, creation, failed write/retry, own list/isolation, done/undo, correction/history, reassignment, cancel/restore preserving ready, empty state, fresh-runtime storage, corrupt storage/reset, untruncated escaped text.');
console.log('NOT browser evidence: keyboard events, native dialog focus, viewport layout and real reload require manual browser checks.');
