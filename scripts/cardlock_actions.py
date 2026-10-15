"""Present Cardlock resources as purposeful, prominent actions."""
from pathlib import Path
import sys
sys.path.insert(0,r'C:\Users\Admin\OneDrive - CWU\AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration\.deps')
from bs4 import BeautifulSoup

def apply(root):
 file=Path(root)/'pacific-pride-card-lock/index.html'
 s=BeautifulSoup(file.read_text(encoding='utf8'),'html.parser')
 if s.select_one('.cardlock-actions'):return
 prose=s.select_one('.prose')
 for p in list(prose.select('p')):
  if 'Sales and Customer Service Please contact' in p.get_text() or any('joyw@' in a.get('href','') or 'rinopacific.com' in a.get('href','') or 'pacificpride.com' in a.get('href','') or '6333-rino-pac-credit-app' in a.get('href','') for a in p.select('a')):p.decompose()
 block=BeautifulSoup('''<section class="cardlock-actions" aria-labelledby="cardlock-action-title"><div class="cardlock-action-heading"><p class="eyebrow">YOUR FLEET. YOUR NEXT MOVE.</p><h2 id="cardlock-action-title">Keep Your Business Rolling.</h2></div><div class="cardlock-action-grid"><a class="cardlock-action cardlock-locator" href="https://pacificpride.com/site-locator/" rel="noopener noreferrer"><img src="../assets/6370-pac-pride-station-image-1.webp" alt="" loading="lazy" decoding="async"><div class="cardlock-action-copy"><span class="cardlock-kicker">THE NEXT STOP</span><h3>Find Fuel On Your Route.</h3><p>Search Pacific Pride locations by area, fuel type and site amenities.</p><span class="cardlock-action-label">Explore Fueling Locations</span></div></a><a class="cardlock-action cardlock-credit" href="../assets/6333-rino-pac-credit-app-new.pdf"><div class="cardlock-document" aria-hidden="true"><img src="../assets/6338-rino-truck-4-1-of-1.webp" alt="" width="1600" height="900" loading="lazy" decoding="async"><div class="cardlock-application-badge"><svg viewBox="0 0 64 72" fill="none"><path d="M13 3h27l13 14v51H13z"/><path d="M40 3v15h13M23 32h20M23 43h20M23 54h13"/></svg><span><strong>Rino Pacific</strong><small>Credit Application</small></span></div></div><div class="cardlock-action-copy"><span class="cardlock-kicker">GET STARTED</span><h3>Put Cardlock To Work.</h3><p>Get the Rino Pacific credit application and take the next step for your fleet.</p><span class="cardlock-action-label">Open Credit Application <small>PDF</small></span></div></a></div><div class="cardlock-sales"><div><p class="eyebrow">A REAL PERSON. A CLEAR NEXT STEP.</p><h3>Talk Fuel With Joy.</h3><p>Joy Williams, Sales &amp; Customer Service</p></div><div class="cardlock-sales-actions"><a href="tel:+17074628811"><small>Call Joy</small><strong>(707) 462-8811</strong></a><a href="mailto:joyw@rinehartoil.com"><small>Email Joy</small><strong>joyw@rinehartoil.com</strong></a></div></div></section>''','html.parser')
 prose.append(block.section)
 file.write_text(str(s),encoding='utf8')
if __name__=='__main__':apply(Path(__file__).resolve().parents[1])
