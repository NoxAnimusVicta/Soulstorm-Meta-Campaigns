'use strict';
let data=JSON.parse(document.getElementById('campaign-data').textContent);
let view='overview', query='', selectedSystem=null, systemScroll=0;
const tabState={};
const main=document.getElementById('main');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function heading(k,title,sub=''){return `<p class="eyebrow">${k}</p><h1>${title}</h1>${sub?`<p class="subtitle">${sub}</p>`:''}`;}
function render(){
 document.getElementById('header-cycle').textContent=String(data.cycle).padStart(2,'0');
 document.querySelectorAll('[data-view]').forEach(b=>{if(b.dataset.view===view)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current');});
 document.getElementById('revision').textContent=`Cycle ${data.cycle} · ${data.status.updated}`;
 if(view==='overview'){
 const nextLog=data.cycle+(3-data.cycle%3);
 main.innerHTML=heading('THE DESSICA CAMPAIGN','Command overview')+`<section class="cycle-banner" aria-label="Current cycle"><div class="cycle-number">${String(data.cycle).padStart(2,'0')}<small>CYCLE</small></div><div><p class="kicker">CAMPAIGN STATUS</p><h2>${esc(data.status.phase)}</h2><p>Next: ${esc(data.status.nextFaction)}</p></div><span class="pill">${data.cycle%3===0?'Logistics Cycle':'Next logistics · Cycle '+nextLog}</span></section><div class="section-head"><h2>Major factions</h2><span>Turn order · I → II → III</span></div><div class="factions">${data.factions.map((f,i)=>{
 const v=f.values,s=Number(v['Supplies (1-100)']),m=Number(v['Manpower (1-100)']);
 return `<article class="faction" style="--accent:var(${['--green','--cyan','--purple'][i]||'--gold'})"><p class="kicker">${['I / IMPERIUM','II / T’AU','III / TYRANID'][i]||'ALLIED FACTION'}</p><h3>${esc(f.name)}</h3><div class="metrics">${[[s,'Supply'],[m,'Manpower']].map(([n,label])=>`<div class="metric"><strong>${esc(n)}</strong><span>${label} / 100</span><div class="meter"><i style="width:${Math.max(0,Math.min(100,n))}%"></i></div></div>`).join('')}</div><details class="faction-details"><summary>Fleets & holdings</summary><dl>${['Fleets','Planets Controlled','Constructions'].map(k=>`<dt>${k==='Planets Controlled'?'Holdings':k}</dt><dd>${esc(v[k])}</dd>`).join('')}${i===2?'<dt>Mobile capital</dt><dd>See Star-Mother status below</dd>':''}</dl></details></article>`;
 }).join('')}</div><div class="section-head"><h2>Cycle dispatch</h2><span>Official campaign record</span></div><div class="brief-grid"><section class="panel"><p class="kicker">EVENT REPORT</p><h2>${esc(data.status.event)}</h2><p class="muted">${esc(data.status.notes)}</p></section><section class="panel"><p class="kicker">LOGISTICS SCHEDULE</p><p>Income and fleet maintenance every third Cycle.</p><div class="timeline">${Array.from({length:6},(_,i)=>{let n=data.cycle+i;return `<span class="${i===0?'current':n%3===0?'logistics':''}" title="Cycle ${n}${n%3===0?' · Logistics':''}">${n}</span>`;}).join('')}</div></section></div><div class="section-head"><h2>Mobile assets</h2></div><div class="article">${data.mobile}</div>`;
 }else if(view==='systems'){
 if(selectedSystem!==null){const s=data.systems[selectedSystem];main.innerHTML=`<button class="back" id="back">← All systems</button>`+heading('SYSTEM DOSSIER',esc(s.title.split(' System')[0]))+`<div class="article">${s.html}</div>`;document.getElementById('back').onclick=()=>{selectedSystem=null;render();window.scrollTo(0,systemScroll);};}
 else{main.innerHTML=heading('SUBSECTOR REGISTER','Systems & holdings',`${data.systems.length} systems · ${data.systems.reduce((n,s)=>n+s.worlds.length,0)} planetary and station holdings`)+`<div class="search-tools"><label for="search" class="sr-only">Search systems, worlds or controllers</label><input class="search" id="search" type="search" placeholder="Search systems, worlds, factions…" value="${esc(query)}" enterkeyhint="search" autocapitalize="none" spellcheck="false"></div><div id="results"></div>`;renderSystems();bindSearch(renderSystems);}
 }else if(view==='rules'){
 main.innerHTML=heading('FIELD MANUAL','Campaign rules','The campaign’s rules, preserved as written.')+`<div class="search-tools"><label for="search" class="sr-only">Search campaign rules</label><input id="search" class="search" type="search" placeholder="Search fleet actions, costs, events…" value="${esc(query)}" enterkeyhint="search" autocapitalize="none" spellcheck="false"></div><div id="results"></div>`;renderRules();bindSearch(renderRules);
 }else{
 main.innerHTML=heading('REGIMENTAL ARCHIVE','Campaign record',`Cycle ${data.cycle} · ${esc(data.status.updated)}`)+`<div class="record-actions"><a href="./Dessica_Campaign.md" download>Download Markdown ↗</a><button id="full">Read complete document</button></div><div class="panel"><p class="kicker">CURRENT POSITION</p><h2>${esc(data.status.phase)}</h2><p>${esc(data.status.notes)}</p></div><div class="section-head"><h2>Battle log</h2></div><div class="article">${data.log}</div>`;
 document.getElementById('full').onclick=()=>{main.innerHTML='<button class="back" id="back">← Campaign record</button><div class="article">'+data.document+'</div>';document.getElementById('back').onclick=render;};
 }
}
function bindSearch(fn){const input=document.getElementById('search');input.oninput=e=>{query=e.target.value;fn();};input.onkeydown=e=>{if(e.key==='Enter'){e.preventDefault();input.blur();}};}
function renderSystems(){
 const matches=data.systems.map((s,i)=>({...s,index:i})).filter(s=>(s.title+' '+s.text).toLowerCase().includes(query.toLowerCase()));
 document.getElementById('results').innerHTML=`<p class="count">${matches.length} systems</p><div class="system-grid">${matches.map(s=>`<article class="system-card"><p class="kicker">SYSTEM / ${String(s.index+1).padStart(2,'0')}</p><h2>${esc(s.title.split(' System')[0])}</h2><p class="muted">${esc(s.title.split(' System ')[1]||'').replace(/^\(|\)$/g,'')}</p><div class="worlds">${s.worlds.map(w=>`<div class="world-row"><div><strong>${esc(w.Planet)}</strong><small>${esc(w.Controller)}</small></div><div><strong>${esc(w.Defense)}</strong><small>${esc(w.Type)}</small></div></div>`).join('')}</div><button data-system="${s.index}">Open dossier ↗</button></article>`).join('')}</div>${matches.length?'':'<p class="empty">No matching systems. Try a planet or faction name.</p>'}`;
 document.querySelectorAll('[data-system]').forEach(b=>b.onclick=()=>{systemScroll=window.scrollY;selectedSystem=Number(b.dataset.system);render();window.scrollTo(0,0);});
}
function renderRules(){
 const matches=data.rules.filter(r=>(r.title+' '+r.text).toLowerCase().includes(query.toLowerCase()));
 document.getElementById('results').innerHTML=`<p class="count">${matches.length} rule entries${query?' match your search':''}</p>`+matches.map(r=>`<details class="rule"><summary>${esc(r.title)}</summary><div class="article">${r.html}</div></details>`).join('')+(matches.length?'':'<p class="empty">No matching rules. Try “Manpower”, “Defend” or “Fleet”.</p>');
}
document.querySelectorAll('[data-view]').forEach(b=>b.onclick=()=>{const target=b.dataset.view;if(target===view){window.scrollTo(0,0);return;}tabState[view]={query,selectedSystem,scroll:window.scrollY};view=target;const state=tabState[view]||{};query=state.query||'';selectedSystem=state.selectedSystem??null;render();window.scrollTo(0,state.scroll||0);});
let checking=false;
async function refresh(){
 if(checking||location.protocol==='file:')return;
 checking=true;const status=document.getElementById('connection');status.textContent='Checking campaign…';
 const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),8000);
 try{
  const res=await fetch('./campaign.json',{cache:'no-store',signal:controller.signal});if(!res.ok)throw Error('Unavailable');const next=await res.json();
  if(!next.revision||!Array.isArray(next.systems)||!next.status)throw Error('Invalid campaign');
  if(next.revision!==data.revision){data=next;render();}
  status.textContent=res.headers.get('X-Dessica-Cache')==='offline'?'Connection unavailable · saved campaign':'Latest published campaign';
 }catch(e){status.textContent='Offline or unavailable · showing saved campaign';}
 finally{clearTimeout(timer);checking=false;}
}
document.getElementById('refresh').onclick=async()=>{await refresh();if('serviceWorker'in navigator){const reg=await navigator.serviceWorker.getRegistration();if(reg)await reg.update();}};
document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')refresh();});
window.addEventListener('online',refresh);window.addEventListener('offline',()=>{document.getElementById('connection').textContent='Offline · showing saved campaign';});
if('serviceWorker'in navigator&&location.protocol!=='file:'){navigator.serviceWorker.register('./sw.js').catch(()=>{});}
render();refresh();setInterval(()=>{if(document.visibilityState==='visible')refresh();},60000);
