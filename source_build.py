"""Build the reusable source reference separately from live campaign state."""
import html
import re
import shutil
import zipfile

DOCUMENTS = [
 ('Source_README.md', 'Start here'),
 ('Source_Rules.md', 'Rules baseline'),
 ('Balance_Simulation_Report.md', 'Simulation results'),
 ('Balance_Simulation_Methods.md', 'Simulation coverage'),
 ('Campaign_Template.md', 'Blank campaign'),
 ('Briefing_Commander_Template.md', 'Commander briefing'),
 ('Briefing_Advisor_Template.md', 'Advisor briefing'),
 ('Faction_Control_Handover_Template.md', 'Control handover'),
 ('Game_Master_Guide.md', 'Game Master guide'),
 ('Campaign_Notes_2026-09-15.md', 'Dated design notes'),
]

def build_source(root, out, render):
    shutil.copyfile(root / "Balance_Simulation_Bundle.zip", out / "Balance_Simulation_Bundle.zip")
    cards = []
    for filename, label in DOCUMENTS:
        text = (root / filename).read_text(encoding='utf-8')
        shutil.copyfile(root / filename, out / filename)
        sections = re.split(r'(?=^## )', text, flags=re.M)
        content = []
        for section in sections:
            lines = section.strip().splitlines()
            if not lines:
                continue
            if lines[0].startswith('## '):
                content.append('<details class="chapter"><summary>' + html.escape(lines[0][3:]) + '</summary>' + render('\n'.join(lines[1:])) + '</details>')
            else:
                content.append(render(section))
        cards.append('<article id="'+filename[:-3]+'"><h2>'+label+'</h2><a download href="./'+filename+'">Download Markdown ↗</a>'+''.join(content)+'</article>')
    with zipfile.ZipFile(out / 'Campaign_Source_v0.1.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for filename, _ in DOCUMENTS:
            archive.write(root / filename, filename)
    navigation = ''.join('<a href="#'+name[:-3]+'">'+label+'</a>' for name,label in DOCUMENTS)
    page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#101715"><title>Soulstorm • Source Library</title><style>
    :root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;background:#101715;color:#e2e8df;font:16px/1.65 system-ui,sans-serif}main{max-width:1050px;margin:auto;padding:24px 20px 70px}a{color:#dcc18a;overflow-wrap:anywhere}header{border-bottom:1px solid #64715c;padding-bottom:20px}h1{font-size:clamp(1.8rem,5vw,3rem);line-height:1.15}h2,h3,h4{color:#ddc392}nav{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0}nav a,.download{display:inline-block;padding:10px 14px;border:1px solid #5c6654;border-radius:6px}input{width:100%;padding:14px;background:#1a241f;color:inherit;border:1px solid #879177;border-radius:6px;font:inherit}article{margin-top:26px;padding:20px;background:#17221c;border:1px solid #394a3b;border-radius:10px}summary{cursor:pointer;padding:12px 4px;font-weight:650;color:#d8c296}details{border-top:1px solid #435140;margin-top:12px}details p{margin:10px 0}table{border-collapse:collapse;min-width:550px;width:100%;font-size:.92rem}td,th{text-align:left;vertical-align:top;border:1px solid #475343;padding:9px}.table-scroll{overflow:auto;margin:14px 0}article[hidden]{display:none}.status{color:#ddc392}a:focus-visible,summary:focus-visible,input:focus-visible{outline:3px solid #d9bd79;outline-offset:3px}@media(max-width:600px){main{padding:16px 12px 50px}article{padding:14px}nav a{font-size:.9rem}h2{font-size:1.4rem}}
    </style><main><header><a href="./index.html">← Dessica campaign</a><h1>Soulstorm Source Library</h1><p class="status">Version 0.1 · 15 September 2026 · Provisional development baseline</p><p>Dessica is suspended at Cycle 21. This separate reference contains reusable rules, blank templates and dated design notes. Proposed balance changes remain open for review.</p><a class="download" download href="./Campaign_Source_v0.1.zip">Download all source documents</a> <a class="download" download href="./Balance_Simulation_Bundle.zip">Download simulation code &amp; data</a><nav aria-label="Source documents">'''+navigation+'''</nav><label for="search">Search the source library</label><input type="search" id="search" placeholder="Rules, briefings, construction…"><p id="matches" aria-live="polite"></p></header>'''+''.join(cards)+'''</main><script>
    const search=document.querySelector('#search');const articles=[...document.querySelectorAll('article')];
    search.addEventListener('input',()=>{const q=search.value.trim().toLowerCase();let count=0;articles.forEach(a=>{a.hidden=!!q&&!a.textContent.toLowerCase().includes(q);if(!a.hidden)count++;a.querySelectorAll('details').forEach(d=>{d.open=!!q&&d.textContent.toLowerCase().includes(q)})});document.querySelector('#matches').textContent=q?count+' matching documents':''});
    document.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{search.value='';search.dispatchEvent(new Event('input'))}));
    </script></html>'''
    (out / 'source.html').write_text(page, encoding='utf-8')
    return page
