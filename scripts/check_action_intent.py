"""Validate owner-requested artwork actions, not merely valid destinations."""
from pathlib import Path
import sys
sys.path.insert(0, r'C:\Users\Admin\OneDrive - CWU\AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration\.deps')
from bs4 import BeautifulSoup

def check(root):
    root = Path(root)
    expected = [
        ('pacific-pride-card-lock/index.html', 'talk-with-joy.jpg', '#joy-contact-options'),
        ('pacific-pride-card-lock/index.html', 'pacific-pride.jpg', 'https://pacificpride.com/site-locator/'),
        ('pacific-pride-card-lock/index.html', 'credit-app.jpg', '../assets/6333-rino-pac-credit-app-new.pdf'),
        ('index.html', 'our-roots-run-deep.jpg', 'about/index.html'),
        ('index.html', '24-7-fuel-transport.jpg', 'trucking-for-hire/index.html'),
        ('index.html', 'company-owned-fleet.jpg', 'fleet/index.html'),
        ('contact/index.html', 'ask-our-team.jpg', '#team'),
        ('customer-resources/index.html', 'ask-our-team.jpg', '../contact/index.html#team'),
        ('contact/index.html', 'call-dispatch.jpg', 'tel:+17074673313'),
        ('contact/index.html', 'main-office.jpg', '#office-call-options'),
        ('contact/index.html', 'email-dispatch.jpg', 'mailto:dispatch@rinehartoil.com'),
        ('index.html', 'rinehart-history.jpg', 'about/index.html'),
        ('index.html', 'check-out-our-fleet.jpg', 'fleet/index.html'),
        ('index.html', 'put-us-to-work.jpg', 'contact/index.html'),
        ('index.html', 'find-your-fuel-solution.jpg', '#services'),
        ('unbranded-fuels/index.html', 'discuss-your-fuel-supply.jpg', '../contact/index.html'),
    ]
    for page, image, target in expected:
        soup = BeautifulSoup((root / page).read_text(encoding='utf8'), 'html.parser')
        matches = soup.select(f'img[src$="/{image}"]')
        assert len(matches) == 1, f'{page}: expected one {image}, found {len(matches)}'
        anchor = matches[0].find_parent('a')
        assert anchor and anchor.get('href') == target, f'{page}: {image} must link to {target}'
    joy = BeautifulSoup((root/'pacific-pride-card-lock/index.html').read_text(encoding='utf8'), 'html.parser')
    assert {a.get('href') for a in joy.select('#joy-contact-options a')} == {'tel:+17074628811', 'mailto:joyw@rinehartoil.com'}, 'Joy chooser must offer call and email'
    assert not joy.select('.cardlock-sales-actions'), 'Move Joy actions into the chooser'
    contact = BeautifulSoup((root/'contact/index.html').read_text(encoding='utf8'), 'html.parser')
    assert not contact.select('.office-secondary'), 'Remove separate toll-free strip'
    assert {a.get('href') for a in contact.select('#office-call-options a')} == {'tel:+17074628811', 'tel:+18006408814'}, 'Offer both approved office numbers'
    assert len(contact.select('.bottom-cta .contact-keep-moving img[src$="/keep-you-moving.jpg"]')) == 1, 'Contact needs its owner-selected companion artwork'
    assert not contact.select('.bottom-cta a'), 'Contact must not contain a bottom Contact button'
    assert len(contact.select('.contact-disclosure')) == 4, 'Preserve three department sections and office hours'
    assert contact.select_one('.contact-location iframe'), 'Address must have a visible map'
    assert not contact.select_one('.contact-location').find_parent('details'), 'Location must not be collapsed'
    assert not contact.select('.contact-disclosure[open]'), 'Directory must start collapsed'
    assert len(contact.select('.team-card')) == 9, 'Keep nine currently listed contacts'
    for page in root.rglob('index.html'):
        text = page.read_text(encoding='utf8').lower()
        assert 'julie rinehart' not in text and 'jrinehart@' not in text and 'hr applications' not in text, f'{page}: former HR contact must stay unpublished'
    print(f'PASS {len(expected)} owner artwork destinations and Contact exclusions')

if __name__ == '__main__':
    check(Path(__file__).resolve().parents[1])
