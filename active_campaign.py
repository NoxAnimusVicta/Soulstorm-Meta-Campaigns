"""Adapt the authoritative Atreus Markdown ledger to the existing command app."""
import re,json,hashlib

def section(text,title):
 return text.split('## '+title+'\n',1)[1].split('\n## ',1)[0]
def tables(text):
 blocks=re.findall(r'(?:^\|[^\n]+\n?)+',text,re.M)
 return [[[c.strip() for c in row.strip().strip('|').split('|')] for row in block.splitlines() if not re.match(r'^\|[\s:|\-]+$',row)] for block in blocks]
def chapters(text,render):
 parts=re.split(r'^#{1,3} (.+)\n',text,flags=re.M)
 return [{'title':parts[i],'text':parts[i+1],'html':render(parts[i+1])} for i in range(1,len(parts),2)]
def load_atreus(root,render):
 md=(root/'Atreus_Campaign.md').read_text(encoding='utf-8')
 status=json.loads((root/'atreus-status.json').read_text(encoding='utf-8'))
 status['nextFaction']=status['next_faction']
 status['notes']='Setup complete. Phase 0 has not opened: resolve construction effects, Logistics if due, then events. No actions or battles have occurred.'
 systems=[]
 for name,body in re.findall(r'^### (.+)\n([\s\S]*?)(?=^### |\Z)',section(md,'Systems and holdings'),re.M):
  ts=tables(body);holdings=ts[0];fleets=ts[1]
  worlds=[{'Planet':x[0],'Type':x[1],'Controller':x[2],'Alignment':x[3],'Defense':x[4],'Income':x[5]} for x in holdings[1:]]
  systems.append({'title':name,'worlds':worlds,'fleets':fleets[1:],'text':body,'html':render(body),'void':next((f[1] for f in fleets[1:] if f[1] in status['turn_order']),'Calculate for acting faction')})
 factions=[]
 for name,body in re.findall(r'^### \d+\. (.+)\n([\s\S]*?)(?=^### |\Z)',section(md,'Major faction registers'),re.M):
  fields=dict(tables(body)[0][1:]);resources=re.search(r'(\d+) Supply / (\d+) Manpower',fields['Resources'])
  assert resources,'Missing resources for '+name
  holdings=[[w['Planet'],s['title'],w['Type'],w['Defense'],w['Income']] for s in systems for w in s['worlds'] if w['Controller']==name]
  fleets=[[f[0],s['title'],f[2]] for s in systems for f in s['fleets'] if f[1]==name]
  factions.append({'name':name,'alignment':fields['Alignment'],'trait':fields['Trait'],'effect':fields['Exact effect'],'values':{'Supplies (1-100)':resources[1],'Manpower (1-100)':resources[2]},'registers':{'fleets':fleets,'holdings':holdings,'constructions':[]}})
 # Read only the campaign's frozen appendix, not a changing source-library file.
 appendix=md.split('## Pinned rules appendix\n',1)[1]
 rules=chapters(appendix[appendix.index('# Soulstorm campaign rules'):],render)
 projects=tables(section(md,'Construction register'))
 for faction in factions:
  if projects:
   faction['registers']['constructions']=[row[1:] for row in projects[0][1:] if row[0]==faction['name']]
 revision=hashlib.sha256((md+json.dumps(status,sort_keys=True)).encode()).hexdigest()[:12]
 return {'campaign':'Atreus','cycle':status['cycle'],'status':status,'factions':factions,'systems':systems,'rules':rules,'mobile':'<p>No Mobile Capitals.</p>','log':render(section(md,'Cycle ledger')),'narratives':render(section(md,'Cycle Records')),'document':render(md),'revision':revision}
