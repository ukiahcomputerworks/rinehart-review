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
            cards.append(f'<a class="document-card" data-resource="{category}" href="{html.escape(href,quote=True)}" rel="noopener noreferrer"><span class="document-type">{meta}</span><h3>{html.escape(label)}</h3><span class="document-action">Open</span></a>')
    # Include every retained downloadable document, including applications outside this page.
    known={BeautifulSoup(card,'html.parser').a['href'] for card in cards}
    names={'13566-ROI-COVID-19-PREVENTION-PROGRAM-EMERGENCY-TEMPORARY-STANDARDS.pdf':'COVID-19 Prevention Program, Historical Reference','13569-roi-employment-application_final-uae.pdf':'Rinehart Oil Employee Application','13571-driver-application-with-desc-2019-rev.pdf':'Rinehart Driver Employment Application','6333-rino-pac-credit-app-new.pdf':'Rino Pacific Credit Application','6352-roi-credit-packet.pdf':'Rinehart Oil Credit Application Packet'}
    for path in sorted((root/'assets').iterdir()):
        href='../assets/'+path.name
        if path.suffix.lower() not in {'.pdf','.doc','.docx','.xls','.xlsx'} or href in known:continue
        label=names.get(path.name,path.stem.split('-',1)[-1].replace('-',' ').replace('_',' ').title())
        cards.append(f'<a class="document-card" data-resource="forms" href="{html.escape(href,quote=True)}"><span class="document-type">{path.suffix[1:].upper()} · {max(1,round(path.stat().st_size/1024)):,} KB</span><h3>{html.escape(label)}</h3><span class="document-action">Open</span></a>')
    groups.append(('forms','Applications & Company Documents','Company documents and application packets.'))
    intro='''<section class="resource-hero wrap"><p class="eyebrow">THE RIGHT INFORMATION. WITHIN REACH.</p><h1 class="page-title">Your Business.<br><span>Your Resource Desk.</span></h1><p>Find reference documents, supplier safety libraries and account application information.</p></section><section class="resource-tools wrap"><a href="../credit-application/index.html" class="resource-tool resource-image-tool" aria-label="View Credit Application"><img src="../assets/credit-application-button.jpg" alt="Credit Application, find the application and instructions for opening an account" width="1024" height="410" loading="lazy" decoding="async"></a><a href="../contact/index.html" class="resource-tool resource-image-tool" aria-label="Ask Our Team, Find Your Contact"><img src="../assets/ask-our-team.jpg" alt="Ask Our Team, help finding a specific document or current version" width="1024" height="397" loading="lazy" decoding="async"></a></section>'''
    filters=''.join(f'<button type="button" data-resource-filter="{category}" aria-pressed="false">{title}</button>' for category,title,_ in groups)
    return intro+f'''<section class="resource-library wrap"><div class="library-heading"><div><p class="eyebrow">DOCUMENTS & CONNECTIONS</p><h2>Find What You Need.</h2></div><label class="document-search document-search-hero"><span id="document-search-title">Find Any Document On This Site Here</span><span class="document-search-field"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none"><circle cx="13" cy="13" r="9"></circle><path d="m20 20 9 9"></path></svg><input id="resource-search" type="search" placeholder="Try credit application, driver, SB 1400 or Valero" aria-labelledby="document-search-title" aria-describedby="document-search-help" aria-controls="document-results"></span><small id="document-search-help">Search document titles and resource names. Results update as you type.</small></label></div><div class="resource-filters" role="group" aria-label="Filter resources"><button type="button" data-resource-filter="all" aria-pressed="true">All Resources</button>{filters}</div><p class="library-note">Industry notices are historical reference files, including notices from 2015 and 2016. Confirm current requirements and document versions with the relevant organization. Safety data links open supplier websites.</p><p id="resource-count" aria-live="polite">{len(cards)} Resources</p><div id="document-results" class="document-grid">{''.join(cards)}</div><div id="resource-empty" hidden><h3>No Matching Resources</h3><p>Try a broader search or select All Resources.</p><button type="button" id="resource-reset">Clear Search & Filters</button></div><p class="library-footnote">The source also lists California AB 32 and FUTC implementation, effective January 1, 2015, as historical context.</p></section>'''
