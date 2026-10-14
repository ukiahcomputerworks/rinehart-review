"""Separate downloadable documents from a focused external-connection directory."""
from pathlib import Path
import sys,json,html
from urllib.parse import urlsplit
sys.path.insert(0,r'C:\Users\Admin\OneDrive - CWU\AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration\.deps')
from bs4 import BeautifulSoup
GROUPS=[('industry','Industry Support'),('government','Government Resources'),('sds','Safety Data Sheets')]
UPDATES={
 'California Air Resources Board (CARB) Cap-And-Trade Program':('CARB Cap-And-Invest Program','https://ww2.arb.ca.gov/our-work/programs/cap-and-invest-program','Program information and resources from the California Air Resources Board.'),
 'CFCA California Fuels & Convenience Alliance':('CFCA California Fuels & Convenience Alliance','https://cfca.energy/','California fuel and convenience industry information and member resources.'),
 'PMAA Petroleum Marketers Association Of America':('EMA Energy Marketers Of America','https://www.energymarketersofamerica.org/','Energy marketer industry news, advocacy and association resources.'),
 'SIGMA Society Of Independent Gasoline Marketers Of America':('SIGMA Society Of Independent Gasoline Marketers Of America','https://www.sigma.org/','Resources for independent fuel marketers and convenience retailers.'),
 'WPMA Western Petroleum Marketers Association':('WPMA Western Petroleum Marketers Association','https://www.wpma.com/','Association information, events and resources for petroleum marketers.'),
 'NACS National Association Of Convenience Stores':('NACS National Association Of Convenience Stores','https://www.convenience.org/','Convenience and fuel retail industry information, education and research.'),
 'California Air Resource Board':('California Air Resources Board','https://ww2.arb.ca.gov/','California air-quality and emissions program information.'),
 'California Department Of Alcohol Beverage Control':('California Department Of Alcoholic Beverage Control','https://www.abc.ca.gov/','California alcoholic beverage licensing and agency resources.'),
 'California EPA':('California Environmental Protection Agency','https://calepa.ca.gov/','California environmental agency information and program connections.'),
 'California Board Of Equalization':('California Board Of Equalization','https://www.boe.ca.gov/','Agency services, tax information and public resources.'),
 'California Water Resources Control Board':('State Water Resources Control Board','https://www.waterboards.ca.gov/','California water-quality and water-board program resources.'),
 'California Department Of Energy':('California Energy Commission','https://www.energy.ca.gov/','California energy policy, planning and program information.'),
 'California Department Of Industrial Relations':('California Department Of Industrial Relations','https://www.dir.ca.gov/','California workplace and industrial-relations information.'),
 'California Legislative Information':('California Legislative Information','https://leginfo.legislature.ca.gov/','Find California bills, laws and legislative information.'),
 'Phillips 66 Safety Data Sheets':('Phillips 66 Safety Data Sheets','https://www.phillips66.com/safety-data-sheets/','Open the supplier’s product safety-data resources.'),
 'Valero Safety Data Sheets':('Valero Safety Data Sheets','https://www.valero.com/responsibility/safety/safety-data-sheets','Search the supplier’s product safety-data documentation.'),
 'Chevron Safety Data Sheets':('Chevron Safety Data Sheets','https://cglapps.chevron.com/msdspds/MSDSPage.aspx?language=en&country=&region=NA','Find product safety-data documentation in the supplier’s library.')}

def switch(active):
 return '<nav class="resource-page-switch wrap" aria-label="Resource Pages">'+''.join(f'<a href="../{route}/index.html" '+('aria-current="page"' if kind==active else '')+f'>{label}</a>' for kind,route,label in [('documents','customer-resources','Documents'),('links','resource-links','Links')])+'</nav>'

def apply(root):
 root=Path(root);file=root/'customer-resources/index.html';s=BeautifulSoup(file.read_text(encoding='utf8'),'html.parser')
 cards=list(s.select('.document-card'));external=[]
 for card in cards:
  if card['href'].startswith('../assets/'):continue
  old=card.h3.get_text();label,url,description={key.casefold():value for key,value in UPDATES.items()}[old.casefold()]
  external.append({'title':label,'url':url,'description':description,'group':'government' if card['data-resource']=='news' else card['data-resource']})
  card.decompose()
 links=BeautifulSoup(str(s),'html.parser')
 s.select_one('.resource-hero').find('p',class_=None).string='Download applications, company documents and historical reference files.'
 s.select_one('.resource-hero').insert_after(BeautifulSoup(switch('documents'),'html.parser').nav)
 s.select_one('#resource-search')['placeholder']='Try credit application, driver or SB 1400'
 s.select_one('#document-search-help').string='Search document titles. Matching categories open as you type.'
 s.select_one('.resource-search-area .eyebrow').string='DOCUMENTS & FORMS'
 library=s.select_one('.resource-library');library['data-resource-kind']='Documents'
 filters=s.select_one('.resource-filters');filters.clear()
 for key,label in [('all','All Documents'),('news','Historical Notices'),('forms','Applications & Company Documents')]:
  button=s.new_tag('button',attrs={'type':'button','data-resource-filter':key,'aria-pressed':'true' if key=='all' else 'false'});button.string=label;filters.append(button)
 for key,label in GROUPS:
  a=s.new_tag('a',href=f'../resource-links/index.html#{key}');a.string=label;hint=s.new_tag('small');hint.string='Links';a.append(hint);filters.append(a)
 results=s.select_one('#document-results');results['class']=['document-groups']
 for key,title,slug in [('forms','Applications & Company Documents','applications'),('news','Historical Notices','historical')]:
  matching=list(results.select(f'[data-resource="{key}"]'))
  detail=s.new_tag('details',attrs={'class':'document-folder','id':slug})
  summary=s.new_tag('summary');summary.string=title
  count=s.new_tag('span',attrs={'class':'folder-count'});count.string=f'{len(matching)} Documents';summary.append(count);detail.append(summary)
  grid=s.new_tag('div',attrs={'class':'document-grid'})
  for card in matching:grid.append(card.extract())
  detail.append(grid);results.append(detail)
 s.select_one('.library-note').string='Historical notices are retained reference files. Confirm current requirements and versions with the relevant organization.'
 s.select_one('.library-footnote').decompose()
 s.select_one('#resource-count').string=f'{len(s.select(".document-card"))} Documents'
 s.select_one('#resource-empty h3').string='No Matching Documents'
 file.write_text(str(s),encoding='utf8')
 # Reuse the same header/footer shell; the links directory has its own focused content.
 links.title.string='Industry & Government Links | Rinehart Oil'
 main=links.select_one('main');main.clear()
 head=BeautifulSoup('<section class="page-head wrap"><p class="eyebrow">RINEHART OIL / BUILT ON DEPENDABILITY</p><h1 class="page-title">Industry Links.<br>Trusted Connections.</h1><p>Government resources, industry organizations and supplier safety-data libraries.</p></section>','html.parser')
 main.append(head.section);main.append(BeautifulSoup(switch('links'),'html.parser').nav)
 buttons=[];options=[];panels=[];fallback=[]
 for group,title in GROUPS:
  items=[(i,item) for i,item in enumerate(external) if item['group']==group]
  options.append(f'<optgroup label="{title}">')
  buttons.append(f'<div class="connection-choice-group" id="{group}" data-connection-group="{group}"><h3>{title}</h3>')
  for i,item in items:
   name=html.escape(item['title']);url=html.escape(item['url'],quote=True);desc=html.escape(item['description']);domain=html.escape(urlsplit(item['url']).hostname or '')
   ident=f'connection-{i}';options.append(f'<option value="{ident}">{name}</option>')
   buttons.append(f'<button type="button" class="connection-choice" data-connection="{ident}" data-group="{group}" aria-controls="{ident}" aria-pressed="false"><span>{i+1:02d}</span>{name}</button>')
   mark={'industry':'IND','government':'CA','sds':'SDS'}[group]
   panels.append(f'<section class="connection-file" id="{ident}" data-group="{group}" hidden aria-labelledby="{ident}-title"><div class="connection-file-heading"><span class="connection-seal" aria-hidden="true">{mark}</span><div><p class="eyebrow">{title}</p><h2 id="{ident}-title">{name}</h2></div></div><p>{desc}</p><small class="connection-domain">{domain}</small><a class="connection-open" href="{url}" rel="noopener noreferrer">Open {"Safety Data Library" if group=="sds" else "Official Website"}</a></section>')
   fallback.append(f'<a class="connection-fallback" href="{url}" rel="noopener noreferrer">{name}</a>')
  options.append('</optgroup>');buttons.append('</div>')
 controls=''.join(f'<button type="button" data-connection-filter="{g}" aria-pressed="false">{t}</button>' for g,t in GROUPS)
 markup=f'<section class="connections wrap"><div class="connection-filters" aria-label="Connection Categories">{controls}</div><div class="connection-console"><div class="connection-pickers"><label class="connection-select-label" for="connection-select">Choose Your Resource</label><select id="connection-select">{"".join(options)}</select><div class="connection-choices">{"".join(buttons)}</div></div><div class="connection-display" aria-live="polite">{"".join(panels)}</div></div><noscript><style>.connection-console,.connection-filters{{display:none}}</style>{"".join(fallback)}</noscript></section>'
 main.append(BeautifulSoup(markup,'html.parser').section)
 # First connection is usable before the interaction script initializes.
 first=links.select_one('.connection-file');first.attrs.pop('hidden',None)
 dest=root/'resource-links';dest.mkdir(exist_ok=True);(dest/'index.html').write_text(str(links),encoding='utf8')
 (root/'resource-links'/'directory.json').write_text(json.dumps(external,indent=2),encoding='utf8')
 manifest=root/'route-map.json';routes=json.loads(manifest.read_text(encoding='utf8'));routes=[r for r in routes if r['target'] not in ['/resource-links/index.html','resource-links/index.html']];routes.append({'source':'/resource-links/','target':'resource-links/index.html','disposition':'owner-requested external links directory; documents retained at customer-resources'});manifest.write_text(json.dumps(routes,indent=2),encoding='utf8')
if __name__=='__main__':apply(Path(__file__).resolve().parents[1])
