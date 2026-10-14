"""Preserve familiar source photography in useful desktop space, stack naturally on phones."""
from pathlib import Path
import sys
sys.path.insert(0,r'C:\Users\Admin\OneDrive - CWU\AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration\.deps')
from bs4 import BeautifulSoup
PHOTOS={
 'trucking-for-hire':('6346-rino-truck-6-1-of-1-cropped.webp','Rinehart Tanker Fleet','6338-rino-truck-4-1-of-1.webp','Rinehart On The Road'),
 'branded-fuels':('6345-valero-1-of-1.webp','Branded Fuel Supply','2796-76-pump.webp','76 Fueling'),
 'unbranded-fuels':('6338-rino-truck-4-1-of-1.webp','Company-Owned Fuel Transport','6346-rino-truck-6-1-of-1-cropped.webp','Ready For Your Next Delivery'),
 'pacific-pride-card-lock':('6370-pac-pride-station-image-1.webp','Pacific Pride Commercial Fueling','2796-76-pump.webp','Fueling Your Operation'),
 'about':('6373-old-time-station-1.webp','A Familiar Piece Of Our Website History','6338-rino-truck-4-1-of-1.webp','The Rinehart Name On The Road'),
 'employment-opportunities':('6346-rino-truck-6-1-of-1-cropped.webp','Drive With Rinehart','6338-rino-truck-4-1-of-1.webp','Company Trucks. Real Opportunity.'),
 'employment-application':('6338-rino-truck-4-1-of-1.webp','The Team Behind Every Delivery','6346-rino-truck-6-1-of-1-cropped.webp','A Fleet Built To Deliver'),
 'employment-application/office-positions':('6338-rino-truck-4-1-of-1.webp','Support Every Delivery','6346-rino-truck-6-1-of-1-cropped.webp','Rinehart Oil'),
 'employment-application/rroi-webpagecontentdriver-application-with-desc-2019-revpdf':('6346-rino-truck-6-1-of-1-cropped.webp','Rinehart Driver Opportunities','6338-rino-truck-4-1-of-1.webp','Company-Owned Fleet'),
 'credit-application':('6345-valero-1-of-1.webp','Fuel For Your Business','6338-rino-truck-4-1-of-1.webp','Dependable Fuel Transport')}
def apply(root):
 root=Path(root)
 for route,(hero,hero_caption,detail,detail_caption) in PHOTOS.items():
  prefix='../'*len(route.split('/'))
  rail_title='Join The Rinehart Team.' if 'employment' in route else ''
  rail_link=f'{prefix}employment-opportunities/index.html' if 'employment' in route else f'{prefix}contact/index.html'
  rail_action='View Opportunities' if 'employment' in route else 'Talk To Rinehart'
  file=root/route/'index.html';s=BeautifulSoup(file.read_text(encoding='utf8'),'html.parser');prefix='../'*len(route.split('/'))
  if s.select_one('.source-photo-rail'):continue
  head=s.select_one('.page-head');head['class']=head.get('class',[])+['photo-page-head']
  photo=BeautifulSoup(f'<figure class="source-header-photo"><img src="{prefix}assets/{hero}" alt="{hero_caption}" decoding="async"><figcaption>{hero_caption}</figcaption></figure>','html.parser')
  head.append(photo.figure)
  content=s.select_one('.page-content');prose=content.select_one('.prose')
  if prose:
   layout=s.new_tag('div',attrs={'class':'source-page-layout'});prose.wrap(layout)
   rail=BeautifulSoup(f'<aside class="source-photo-rail" aria-label="Rinehart Photography"><figure><a href="{prefix}assets/{detail}" aria-label="View {detail_caption}"><img src="{prefix}assets/{detail}" alt="{detail_caption}" loading="lazy" decoding="async"></a><figcaption>{detail_caption}</figcaption></figure><div class="photo-rail-contact"><p class="eyebrow">LET’S GET TO WORK</p><h2>{rail_title}</h2><a href="{rail_link}">{rail_action} </a><a href="{prefix}fleet/index.html">See Our Fleet </a></div></aside>','html.parser');layout.append(rail.aside)
   panel=layout.select_one('.photo-rail-contact')
   if 'employment' not in route:
    panel.clear()
   else:
    for link in list(panel.select('a')):
     if 'fleet/index.html' in link.get('href',''):link.decompose()
     else:link['class']=['career-action']
   action=BeautifulSoup(f'<a class="fleet-action fleet-art-button" href="{prefix}fleet/index.html" aria-label="Check Out Our Fleet"><img src="{prefix}assets/fleet-button-industrial.png" alt="Check Out Our Fleet — Rinehart tanker trucks in an industrial steel frame" width="1024" height="254" loading="lazy" decoding="async"></a>','html.parser')
   panel.append(action.a)
  file.write_text(str(s),encoding='utf8')
 # Keep these original photos on their matching detail pages, without a redundant home row.
 file=root/'index.html';s=BeautifulSoup(file.read_text(encoding='utf8'),'html.parser')
 for panel in s.select('.familiar-photos'):panel.decompose()
 file.write_text(str(s),encoding='utf8')
 # Fleet: retain all owner photos and add the original website's two fleet portraits.
 file=root/'fleet/index.html';s=BeautifulSoup(file.read_text(encoding='utf8'),'html.parser');gallery=s.select_one('.fleet-gallery')
 if not s.select_one('.source-fleet-photo'):
  for image,caption in [('6346-rino-truck-6-1-of-1-cropped.webp','Rinehart Tanker From Our Original Website'),('6338-rino-truck-4-1-of-1.webp','A Familiar Rinehart Fleet Photograph')]:
   card=BeautifulSoup(f'<figure class="source-fleet-photo"><a href="../assets/{image}"><img src="../assets/{image}" alt="{caption}" loading="lazy"></a><figcaption>{caption}</figcaption></figure>','html.parser');gallery.insert(0,card.figure)
  file.write_text(str(s),encoding='utf8')
if __name__=='__main__':apply(Path(__file__).resolve().parents[1])
