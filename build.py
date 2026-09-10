from pathlib import Path
import re, json, html, hashlib, shutil
ROOT=Path(__file__).parent
OUT=ROOT/'dist'; OUT.mkdir(exist_ok=True)
md=(ROOT/'Dessica_Campaign.md').read_text()
def inline(s):
 s=html.escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
 return re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<em>\1</em>',s)
def cells(line): return [x.strip() for x in line.strip().strip('|').split('|')]
def table_rows(text):
 return [cells(l) for l in text.splitlines() if l.startswith('|') and not re.match(r'^\|[\s:|\-]+$',l)]
def render(text):
 lines=text.splitlines(); out=[]; i=0
 while i<len(lines):
  s=lines[i].strip()
  if not s: i+=1; continue
  if s.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    if not re.match(r'^\|[\s:|\-]+$',lines[i].strip()): rows.append(cells(lines[i]))
    i+=1
   out.append('<div class="table-scroll" tabindex="0"><table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td data-label="'+html.escape(rows[0][j] if j<len(rows[0]) else '',quote=True)+'">'+inline(c)+'</td>' for j,c in enumerate(row))+'</tr>' for row in rows[1:])+'</tbody></table></div>'); continue
  if re.match(r'^#{1,6} ',s):
   n=len(s.split(' ')[0]); n=min(n+1,6); out.append(f'<h{n}>'+inline(s.split(' ',1)[1])+f'</h{n}>')
  elif s=='---': out.append('<hr>')
  elif re.match(r'^(- |\d+\. )',s): out.append('<p class="list-line">'+inline(s)+'</p>')
  else: out.append('<p>'+inline(s)+'</p>')
  i+=1
 return '\n'.join(out)
cycle=int(re.search(r'\*\*Current Cycle:\*\* (\d+)',md)[1])
tracker=md.split('### Resource Tracker',1)[1].split('**AI vs AI',1)[0]
rows=table_rows(tracker); factions=[]
for i,name in enumerate(rows[0][1:],1):
 values={r[0]:r[i] for r in rows[1:]}
 factions.append({'name':name,'values':values})
sub=md.split('## The Dessica Subsector',1)[1].split('## Mobile Assets',1)[0]
systems=[]
for match in re.finditer(r'^### (.+)\n([\s\S]*?)(?=^### |\Z)',sub,re.M):
 title,body=match.groups(); worlds=table_rows(body)
 systems.append({'title':title,'worlds':[dict(zip(worlds[0],r)) for r in worlds[1:]],'html':render(body),'text':body})
rules=md.split('## SECTION 1:',1)[1].split('## SECTION 5:',1)[0]
parts=re.split(r'^#{2,4} (.+)\n',rules,flags=re.M); chapters=[]
if parts[0].strip(): chapters.append({'title':'Campaign setup','html':render(parts[0]),'text':parts[0]})
for i in range(1,len(parts),2): chapters.append({'title':parts[i],'html':render(parts[i+1]),'text':parts[i+1]})
status=json.loads((ROOT/'campaign-status.json').read_text())
assert status['cycle']==cycle,'Status and campaign cycle disagree'
data={'cycle':cycle,'status':status,'factions':factions,'systems':systems,'rules':chapters,'mobile':render(md.split('## Mobile Assets',1)[1].split('## Battle Log',1)[0]),'log':render(md.split('## Battle Log',1)[1]),'document':render(md)}
revision=hashlib.sha256((md+json.dumps(status,sort_keys=True)).encode()).hexdigest()[:12]
data['revision']=revision
payload=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
(OUT/'campaign.json').write_text(payload)
page=(ROOT/'index.template.html').read_text().replace('/*__STYLE__*/',(ROOT/'style.css').read_text()).replace('/*__APP__*/',(ROOT/'app.js').read_text()).replace('/*__DATA__*/',payload)
(OUT/'index.html').write_text(page)
shutil.copyfile(ROOT/'Dessica_Campaign.md',OUT/'Dessica_Campaign.md')
for name in ['manifest.webmanifest','icon-180.png','icon-192.png','icon-512.png']:
 shutil.copyfile(ROOT/name,OUT/name)
static_revision=hashlib.sha256(page.encode()).hexdigest()[:12]
(OUT/'sw.js').write_text((ROOT/'sw.template.js').read_text().replace('__REVISION__',static_revision))
(OUT/'.nojekyll').touch()
print(f'Built Cycle {cycle}: {len(factions)} factions, {len(systems)} systems, {sum(len(s["worlds"]) for s in systems)} holdings, {len(chapters)} rule entries. Revision {revision}')
