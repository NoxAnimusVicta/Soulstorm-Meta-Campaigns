"""Build Atreus from its authoritative Markdown, without advancing play."""
import re, html, json, hashlib, shutil, zipfile

FILES=['Atreus_Cycle_02_Phase_0_Rolls.json','Atreus_Cycle_01_Daeira_Battle.json','Atreus_Cycle_01_Olenos_Battle.json','Atreus_Cycle_01_Phase_0_Rolls.json','atreus_orontes_preview.webp','atreus_bell_ringa_preview.webp','atreus_althaia_preview.webp','Unification_Roster_Reference_2026-10-07.md','Atreus_Campaign.md','atreus-status.json','Atreus_Setup_Rolls_2026-10-07.json','Atreus_Setup_Registers.json','briefing_first_paladin_menandros.md','briefing_warboss_bell_ringa.md','briefing_canoness_althaia.md','atreus_orontes.png','atreus_bell_ringa.png','atreus_althaia.png']

def inline(text):
 text=html.escape(text)
 text=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',lambda m:'<img loading="lazy" alt="'+m[1]+'" src="'+m[2]+'">',text)
 text=re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',lambda m:'<a href="'+m[2]+'">'+m[1]+'</a>' if not re.match(r'(?i)(javascript|data):',m[2]) else m[1],text)
 text=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',text)
 return re.sub(r'`([^`]+)`',r'<code>\1</code>',text)

def render(text):
 lines=text.splitlines();out=[];i=0
 while i<len(lines):
  s=lines[i].strip()
  if not s:i+=1;continue
  if s.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    if not re.match(r'^\|[\s:|\-]+$',lines[i].strip()):rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
    i+=1
   assert all(len(row)==len(rows[0]) for row in rows),'Ragged Markdown table'
   out.append('<div class="table-scroll" tabindex="0"><table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td data-label="'+html.escape(rows[0][j],quote=True)+'">'+inline(c)+'</td>' for j,c in enumerate(row))+'</tr>' for row in rows[1:])+'</tbody></table></div>');continue
  h=re.match(r'^(#{1,6}) (.*)',s)
  if h:out.append(f'<h{len(h[1])}>'+inline(h[2])+f'</h{len(h[1])}>')
  elif s=='---':out.append('<hr>')
  else:out.append('<p>'+inline(s)+'</p>')
  i+=1
 return '\n'.join(out)

def build_atreus(root,out):
 md=(root/'Atreus_Campaign.md').read_text(encoding='utf-8')
 status=json.loads((root/'atreus-status.json').read_text(encoding='utf-8'))
 assert status['campaign']=='Atreus'
 assert f'Cycle {status["cycle"]}' in md
 sections=re.split(r'(?=^## )',md,flags=re.M)
 nav=[];body=[]
 for i,s in enumerate(sections):
  if s.startswith('## '):
   title,_,content=s.partition('\n');title=title[3:];ident=f'section-{i}'
   nav.append(f'<a href="#{ident}">{html.escape(title)}</a>')
   body.append(f'<details id="{ident}" class="chapter"><summary>{html.escape(title)}</summary>{render(content)}</details>')
  else:body.append(render(s))
 style='''*{box-sizing:border-box}html{color-scheme:dark;scroll-behavior:smooth}body{margin:0;background:#111719;color:#e6e7df;font:16px/1.6 system-ui,sans-serif}main{max-width:1160px;margin:auto;padding:24px 22px 70px}a{color:#e0bc78;overflow-wrap:anywhere}h1,h2,h3,summary{color:#e4c690}h1{font-size:clamp(2rem,5vw,3.6rem);line-height:1.15}header{border-bottom:1px solid #6d624e;padding-bottom:18px}.eyebrow{letter-spacing:.16em;font-size:.8rem;color:#bfb5a0}nav,.downloads{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0}nav a,.downloads a{padding:7px 11px;border:1px solid #5e6158;border-radius:5px;text-decoration:none}details{padding:12px 18px;margin:12px 0;background:#1a2325;border:1px solid #48534f;border-radius:7px}summary{font-weight:650;font-size:1.12rem;cursor:pointer}table{border-collapse:collapse;width:100%;min-width:540px;font-size:.9rem}th,td{border:1px solid #536059;text-align:left;vertical-align:top;padding:8px}th{background:#242f2d}.table-scroll{overflow:auto;margin:12px 0}img{display:block;max-height:470px;max-width:100%;object-fit:contain;object-position:left;margin:16px 0;border-radius:6px}input{width:100%;padding:12px;font:inherit;color:inherit;background:#101819;border:1px solid #86927b;border-radius:5px}code{overflow-wrap:anywhere;font-size:.9em}.status{color:#d6dcbb}.directory{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px}.system{padding:10px;border:1px solid #4c5b50;background:#1b2525;border-radius:6px}.system strong{display:block;color:#e4c690}a:focus-visible,summary:focus-visible,input:focus-visible{outline:3px solid #e1c384;outline-offset:3px}@media(max-width:600px){main{padding:18px 12px 50px}details{padding:10px}nav a{font-size:.9rem}img{max-height:350px}}'''
 systems=md.split('## Systems and holdings\n',1)[1].split('## Minor faction register',1)[0]
 directory=[]
 for name,content in re.findall(r'^### (.+)\n([\s\S]*?)(?=^### |\Z)',systems,re.M):
  rows=re.findall(r'^\|[^\n]+(?:Planet|Station)\|[^\n]+$',content,re.M)
  directory.append('<div class="system"><strong>'+html.escape(name)+'</strong>'+str(len(rows))+' holdings</div>')
 header='<header><p class="eyebrow">SOULSTORM · IMPERIUM NIHILUS</p><h1>The Atreus Campaign</h1><p class="status">Cycle '+str(status['cycle'])+' · '+html.escape(status['phase'])+'</p><p>Ten systems. Three Major Factions. Service, suspicion and conquest.</p><div class="downloads"><a href="index.html">Campaign command</a><a href="Atreus_Campaign.md" download>Campaign document</a><a href="Atreus_Campaign_Pack_2026-10-07.zip" download>Campaign pack & briefings</a><a href="source.html">Source library</a><details><summary>Archives</summary><a href="archives/dessica-cycle21-20261007/index.html">Dessica · Cycle 21</a></details></div><label for="search">Find a rule, system or faction</label><input id="search" type="search" placeholder="Tiryns, Ground Assault, construction…"><p id="matches" aria-live="polite"></p></header><h2>System directory</h2><p>Roster only: all systems are reachable with normal Fleet Movement. No travel lanes or directional restrictions.</p><div class="directory">'+''.join(directory)+'</div><nav aria-label="Campaign sections">'+''.join(nav)+'</nav>'
 script='''const q=document.querySelector('#search');const chapters=[...document.querySelectorAll('.chapter')];q.addEventListener('input',()=>{const text=q.value.trim().toLowerCase();let n=0;chapters.forEach(c=>{const match=!text||c.textContent.toLowerCase().includes(text);c.hidden=!match;c.open=!!text&&match;if(match)n++});document.querySelector('#matches').textContent=text?n+' matching sections':''});document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{q.value='';q.dispatchEvent(new Event('input'));document.querySelector(a.getAttribute('href')).open=true}));if(location.hash){const el=document.querySelector(location.hash);if(el&&el.tagName==='DETAILS')el.open=true}'''
 page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Atreus · Soulstorm Campaign</title><style>'+style+'</style><main>'+header+''.join(body)+'</main><script>'+script+'</script></html>'
 (out/'atreus.html').write_text(page,encoding='utf-8')
 for fn in FILES:shutil.copyfile(root/fn,out/fn)
 for fn in FILES:
  if fn.startswith('briefing_'):
   (out/(fn[:-3]+'.html')).write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Atreus briefing</title><style>'+style+'</style><main><a href="atreus.html">← Atreus campaign</a> · <a download href="'+fn+'">Download briefing</a>'+render((root/fn).read_text(encoding='utf-8'))+'</main></html>',encoding='utf-8')
 with zipfile.ZipFile(out/'Atreus_Campaign_Pack_2026-10-07.zip','w',zipfile.ZIP_DEFLATED) as z:
  for fn in FILES:z.write(root/fn,fn)
  z.write(root/'Source_Rules_Playtest_2026-10-06.md','Source_Rules_Playtest_2026-10-06.md')
 print('Built Atreus:',status['phase'],'revision',hashlib.sha256(md.encode()).hexdigest()[:12])
 return page
