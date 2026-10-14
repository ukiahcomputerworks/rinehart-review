"""Balance the remaining page layouts without changing service or policy text."""
from pathlib import Path
import sys
sys.path.insert(0,r'C:\Users\Admin\OneDrive - CWU\AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration\.deps')
from bs4 import BeautifulSoup
def apply(root):
 root=Path(root)
 for route,image,caption,selector in [
  ('fleet','6338-rino-truck-4-1-of-1.webp','The Rinehart Name On The Road','.page-head'),
  ('driver-application','6346-rino-truck-6-1-of-1-cropped.webp','Drive With Rinehart','.page-head'),
  ('customer-resources','6345-valero-1-of-1.webp','Resources For Your Fuel Business','.resource-hero')]:
  file=root/route/'index.html'
  if not file.exists():continue
  s=BeautifulSoup(file.read_text(encoding='utf8'),'html.parser');head=s.select_one(selector)
  if head and not head.select_one('.source-header-photo'):
   head['class']=head.get('class',[])+['photo-page-head']
   if head.select_one('p:not(.eyebrow)'):head['class'].append('three-row-head')
   head.append(BeautifulSoup(f'<figure class="source-header-photo"><img src="../assets/{image}" alt="{caption}" decoding="async"><figcaption>{caption}</figcaption></figure>','html.parser').figure)
  if route=='driver-application':
   aside=s.select_one('.application-aside')
   if aside and not aside.select_one('.application-guide'):
    guide=s.new_tag('div',attrs={'class':'application-guide'})
    for child in list(aside.contents):guide.append(child.extract())
    aside.append(guide)
    # Original fleet portrait preserves the familiar equipment instead of a second hero crop.
    guide.select_one('img')['src']='../assets/6338-rino-truck-4-1-of-1.webp'
    guide.select_one('img')['alt']='Rinehart Oil company trucks from the original website'
  file.write_text(str(s),encoding='utf8')
 file=root/'privacy-policy/index.html';s=BeautifulSoup(file.read_text(encoding='utf8'),'html.parser')
 if not s.select_one('.policy-layout'):
  prose=s.select_one('.prose');layout=s.new_tag('div',attrs={'class':'policy-layout'});prose.wrap(layout);prose['class']=prose.get('class',[])+['policy-copy']
  links=[]
  for i,heading in enumerate(prose.select('h2'),1):
   heading['id']=f'privacy-section-{i}';links.append(f'<a href="#privacy-section-{i}">{heading.get_text(strip=True)}</a>')
  nav=BeautifulSoup('<aside class="policy-navigator"><nav aria-label="Privacy Policy Sections"><p class="eyebrow">FIND YOUR ANSWER</p><h2>In This Policy</h2>'+''.join(links)+'</nav><div class="policy-help"><h3>Privacy Questions?</h3><p>Use the contact details in the policy to ask about your information.</p><a href="#privacy-section-8">Contact Rinehart </a></div></aside>','html.parser');layout.append(nav.aside)
  head=s.select_one('.page-head');head['class']=head.get('class',[])+['photo-page-head','policy-page-head']
  head.append(BeautifulSoup('<div class="policy-header-panel"><p class="eyebrow">EFFECTIVE OCTOBER 2026</p><h2>Your Information.<br>Your Choice.</h2><a href="#privacy-section-3">Explore Your Privacy Rights </a><a href="#privacy-section-8">Ask A Privacy Question </a></div>','html.parser').div)
  file.write_text(str(s),encoding='utf8')
 # Remove empty legacy text blocks that create spacing without visible content.
 for file in root.rglob('*.html'):
  s=BeautifulSoup(file.read_text(encoding='utf8'),'html.parser');changed=False
  for prose in s.select('.prose'):
   for el in list(prose.select('p,h3,h4,blockquote')):
    if not el.get_text(strip=True).replace('\u00a0','').strip() and not el.select_one('img,a,input,button'):
     el.decompose();changed=True
  if changed:file.write_text(str(s),encoding='utf8')
if __name__=='__main__':apply(Path(__file__).resolve().parents[1])
