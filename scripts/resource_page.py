import html
from bs4 import BeautifulSoup

def resources(root):
    source=BeautifulSoup((root/'customer-resources/index.html').read_text(encoding='utf8'),'html.parser')
    groups=[('news','Historical Notices','Retained industry notices and company reference files.'),('industry','Industry Support','Fuel and convenience industry organizations.'),('government','Government Resources','Agency and public information links from the source website.'),('sds','Safety Data Sheets','Supplier portals for product safety information.')]
    cards=[]
    for category,title,description in groups:
        section=next((h.parent for h in source.select('.prose h4') if h.get_text(strip=True)=={'news':'Current News','industry':'Industry Support','government':'Government','sds':'SDS'}[category]),None)
        if not section: continue
        for a in section.select('a[href]'):
            href=a['href']; label=a.get_text(' ',strip=True)
            if not label:
                img=a.find('img'); label=({'P66 LOGO':'Phillips 66 Safety Data Sheets','Valero Logo':'Valero Safety Data Sheets','Chevron Logo':'Chevron Safety Data Sheets'}.get(img.get('alt','')) if img else None) or 'Supplier Safety Data Sheets'
            if category=='industry' and a.parent.name=='td': label=a.parent.parent.get_text(' ',strip=True).replace('CFCA CFCA','CFCA')
            path=root/href.replace('../','',1)
            ext=path.suffix.upper().lstrip('.') if href.startswith('../assets/') else 'WEBSITE'
            meta=ext
            if path.exists() and path.is_file(): meta+=f' · {max(1,round(path.stat().st_size/1024)):,} KB'
            if category=='news':meta+=' · Historical Reference'
            cards.append(f'<a class="document-card" data-resource="{category}" href="{html.escape(href,quote=True)}" rel="noopener noreferrer"><span class="document-type">{meta}</span><h3>{html.escape(label)}</h3><span class="document-action">Open {"Document" if ext!="WEBSITE" else "Website"} </span></a>')
    intro='''<section class="resource-hero wrap"><p class="eyebrow">THE RIGHT INFORMATION. WITHIN REACH.</p><h1>Your Business.<br><span>Your Resource Desk.</span></h1><p>Find a reference document, reach a supplier’s safety library, or open the customer tools you use every day.</p></section><section class="resource-tools wrap"><a href="https://www.rinehartoil.com/customer-resources/" class="resource-tool"><small>01 / CUSTOMER TOOL</small><h2>Margin Calculator</h2><p>Use the working calculator on Rinehart’s current website.</p><span>Open Customer Tools </span></a><a href="../credit-application/index.html" class="resource-tool"><small>02 / GET STARTED</small><h2>Credit Application</h2><p>Find the application and instructions for opening an account.</p><span>View Application </span></a><a href="../contact/index.html" class="resource-tool"><small>03 / NEED A HAND?</small><h2>Ask Our Team</h2><p>Need a specific document or a current version? We’ll point you in the right direction.</p><span>Find Your Contact </span></a></section>'''
    filters=''.join(f'<button type="button" data-resource-filter="{category}" aria-pressed="false">{title}</button>' for category,title,_ in groups)
    return intro+f'''<section class="resource-library wrap"><div class="library-heading"><div><p class="eyebrow">DOCUMENTS & CONNECTIONS</p><h2>Find What You Need.</h2></div><label class="document-search">Search The Library<input id="resource-search" type="search" placeholder="Try supply chain, SB 1400, or Valero" aria-controls="document-results"></label></div><div class="resource-filters" role="group" aria-label="Filter resources"><button type="button" data-resource-filter="all" aria-pressed="true">All Resources</button>{filters}</div><p class="library-note">Industry notices are historical reference files, including notices from 2015 and 2016. Confirm current requirements and document versions with the relevant organization. Safety data links open supplier websites.</p><p id="resource-count" aria-live="polite">{len(cards)} Resources</p><div id="document-results" class="document-grid">{''.join(cards)}</div><div id="resource-empty" hidden><h3>No Matching Resources</h3><p>Try a broader search or select All Resources.</p><button type="button" id="resource-reset">Clear Search & Filters</button></div><p class="library-footnote">The source also lists California AB 32 and FUTC implementation, effective January 1, 2015, as historical context.</p></section>'''
