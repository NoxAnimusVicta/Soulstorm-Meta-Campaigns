from pathlib import Path
import re, json, html, hashlib, shutil
ROOT=Path(__file__).parent
OUT=ROOT/'dist'; OUT.mkdir(exist_ok=True)
# Dessica ledger is preserved in the archive; it is not the active data source.
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
# The active app reads Atreus; Dessica is a frozen, independently browsable archive.
from active_campaign import load_atreus
from atreus_build import render as render_atreus, build_atreus
data=load_atreus(ROOT,render_atreus)
revision=data['revision'];cycle=data['cycle']
payload=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
(OUT/'campaign.json').write_text(payload,encoding='utf-8')
page=(ROOT/'index.template.html').read_text(encoding='utf-8').replace('/*__STYLE__*/',(ROOT/'style.css').read_text(encoding='utf-8')).replace('/*__APP__*/',(ROOT/'app.js').read_text(encoding='utf-8')).replace('/*__DATA__*/',payload)
(OUT/'index.html').write_text(page,encoding='utf-8')
for name in ['manifest.webmanifest','atreus-icon-180.png','atreus-icon-192.png','atreus-icon-512.png']:
 shutil.copyfile(ROOT/name,OUT/name)
from source_build import build_source
source_page=build_source(ROOT,OUT,render)
build_atreus(ROOT,OUT)
archive=ROOT/'archives/dessica-cycle21-20261007'
if not archive.exists():
 import zipfile
 with zipfile.ZipFile(ROOT/'Dessica_Archive_Cycle21_2026-10-07.zip') as z:
  archive.mkdir(parents=True)
  z.extractall(archive)
shutil.copytree(archive,OUT/'archives/dessica-cycle21-20261007',dirs_exist_ok=True)
shutil.copyfile(ROOT/'Dessica_Archive_Cycle21_2026-10-07.zip',OUT/'Dessica_Archive_Cycle21_2026-10-07.zip')
static_revision=hashlib.sha256((page+source_page).encode()).hexdigest()[:12]
(OUT/'sw.js').write_text((ROOT/'sw.template.js').read_text().replace('__REVISION__',static_revision))
(OUT/'.nojekyll').touch()
print(f'Built Atreus Cycle {cycle}: {len(data["factions"])} factions, {len(data["systems"])} systems. Revision {revision}')
