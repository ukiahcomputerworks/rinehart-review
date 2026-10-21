"""Guard the transport consolidation, retained contact actions and retirement paths."""
from pathlib import Path
import json, sys
sys.path.insert(0, r'C:\Users\Admin\OneDrive - CWU\AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration\.deps')
from bs4 import BeautifulSoup

def check(root):
    root = Path(root)
    routes = json.loads((root/'route-map.json').read_text(encoding='utf8'))
    rendered = [r for r in routes if r['disposition'] != 'redirect']
    assert len(rendered) == 7 and len(routes) == 17
    artwork = {
        'index.html': {'rinehart-history.jpg':'about/index.html', 'check-out-our-fleet.jpg':'trucking-for-hire/index.html#fleet', 'put-us-to-work.jpg':'contact/index.html'},
        'about/index.html': {'check-out-our-fleet.jpg':'../trucking-for-hire/index.html#fleet'},
        'employment-opportunities/index.html': {'talk-to-rinehart.jpg':'tel:+17074628811'},
        'contact/index.html': {'call-dispatch.jpg':'tel:+17074673313', 'main-office.jpg':'#office-call-options', 'email-dispatch.jpg':'mailto:dispatch@rinehartoil.com'},
        'pacific-pride-card-lock/index.html': {'pacific-pride.jpg':'https://pacificpride.com/site-locator/', 'credit-app.jpg':'../assets/6333-rino-pac-credit-app-new.pdf', 'talk-with-joy.jpg':'#joy-contact-options'}
    }
    for page, images in artwork.items():
        soup = BeautifulSoup((root/page).read_text(encoding='utf8'), 'html.parser')
        for image, destination in images.items():
            matches = soup.select(f'img[src$="/{image}"]')
            assert len(matches) == 1 and matches[0].find_parent('a')['href'] == destination, f'{page}: preserve approved {image} action'
    contact_art = BeautifulSoup((root/'contact/index.html').read_text(encoding='utf8'), 'html.parser')
    assert contact_art.select_one('.directions-image-button img[src$="/directions.jpg"]')
    for route in rendered:
        s = BeautifulSoup((root/route['target']).read_text(encoding='utf8'), 'html.parser')
        assert len(s.select('h1')) == 1
        assert len(s.select('#nav a')) == 5
        assert len(s.select('footer a[href$="pacific-pride-card-lock/index.html"]')) == 1
        assert not s.select('form, input'), 'No unready application collection'
        for link in s.select('a[href]'):
            assert not any(p in link['href'] for p in ('driver-application/index.html','credit-application/index.html','customer-resources/index.html','resource-links/index.html','branded-fuels/index.html','unbranded-fuels/index.html','fleet/index.html')), link['href']
        text = s.get_text(' ',strip=True).lower()
        assert not any(x in text for x in ('julie rinehart', 'hr applications', 'costco', 'spill-free', '24/7', 'supply agreements'))
        assert 'jrinehart@' not in str(s)
    home = BeautifulSoup((root/'index.html').read_text(encoding='utf8'), 'html.parser')
    dispatch_button = home.select_one('.transport-actions .transport-button[href="tel:+17074673313"]')
    assert dispatch_button and 'Dispatch:' in dispatch_button.get_text(' ', strip=True), 'Keep homepage dispatch action as a button'
    contact = BeautifulSoup((root/'contact/index.html').read_text(encoding='utf8'), 'html.parser')
    assert not contact.select('img[src$="/ask-our-team.jpg"]')
    assert {a['href'] for a in contact.select('#office-call-options a')} == {'tel:+17074628811','tel:+18006408814'}
    assert len(contact.select('.team-card')) == 9
    assert contact.select_one('.transport-map iframe')
    assert contact.select_one('.transport-map iframe').find_parent('details')
    assert not contact.select('.bottom-cta')
    transport = BeautifulSoup((root/'trucking-for-hire/index.html').read_text(encoding='utf8'), 'html.parser')
    gallery_sources = {img['src'].rsplit('/', 1)[-1] for img in transport.select('.transport-gallery img[src]')}
    assert {f'owner-{number:02}.webp' for number in range(1, 13)} <= gallery_sources, 'Keep all owner-supplied fleet photos in gallery'
    joy = BeautifulSoup((root/'pacific-pride-card-lock/index.html').read_text(encoding='utf8'), 'html.parser')
    assert {a['href'] for a in joy.select('#joy-contact-options a')} == {'tel:+17074628811', 'mailto:joyw@rinehartoil.com'}
    assert joy.select_one('.joy-image-button')['href'] == '#joy-contact-options'
    print('PASS 7 pages, 10 retirement paths, retained directory, office/Joy choices and HR hold')

if __name__ == '__main__':
    check(Path(__file__).resolve().parents[1])
