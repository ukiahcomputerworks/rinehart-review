"""Keep contact actions inside their panels and remove repeated empty space."""
from pathlib import Path
import sys
sys.path.insert(0, r'C:\Users\Admin\OneDrive - CWU\AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration\.deps')
from bs4 import BeautifulSoup

def apply(root):
    root = Path(root)
    for file in root.rglob('*.html'):
        if any(part in {'scripts', 'source', '.deps', 'templates'} for part in file.relative_to(root).parts):
            continue
        soup = BeautifulSoup(file.read_text(encoding='utf-8'), 'html.parser')
        if file.parent.name in {'trucking-for-hire', 'branded-fuels', 'unbranded-fuels', 'pacific-pride-card-lock'}:
            eyebrow = soup.select_one('.page-head .eyebrow')
            if eyebrow:
                eyebrow.string = 'RINEHART OIL / BUILT ON DEPENDABILITY'
        if file == root / 'index.html':
            for panel in soup.select('.familiar-photos'):
                panel.decompose()
            dispatch = soup.select_one('.dispatch-band')
            hero = soup.select_one('.hero')
            if dispatch and hero:
                dispatch.extract()
                dispatch.name = 'aside'
                dispatch['class'] = ['hero-dispatch']
                dispatch['aria-label'] = 'Contact Dispatch'
                hero.append(dispatch)
        cta = soup.select_one('.bottom-cta')
        if cta and file.parent.name == 'contact':
            action = cta.find('a')
            if action:
                action.decompose()
            if not cta.select_one('.contact-keep-moving'):
                image = soup.new_tag('img', attrs={'src': '../assets/keep-you-moving.jpg', 'alt': 'Rinehart tanker on the road in a riveted steel frame', 'width': '1024', 'height': '254', 'loading': 'lazy', 'decoding': 'async'})
                artwork = soup.new_tag('div', attrs={'class': 'contact-keep-moving'})
                artwork.append(image)
                cta.append(artwork)
        if cta:
            panel = cta.find('div', recursive=False)
            action = cta.find('a', recursive=False) or cta.find(class_='contact-keep-moving', recursive=False)
            if panel and action:
                copy = soup.new_tag('div', attrs={'class': 'cta-copy'})
                for child in list(panel.contents):
                    copy.append(child.extract())
                panel['class'] = ['cta-panel']
                panel.append(copy)
                panel.append(action.extract())
        base = soup.select_one('.footer-base')
        if base and not base.select_one('.client-copyright'):
            for child in list(base.contents):
                if isinstance(child, str) and child.strip().startswith('©'):
                    span = soup.new_tag('span', attrs={'class': 'client-copyright'})
                    span.string = child.strip()
                    child.replace_with(span)
                    break
        file.write_text(str(soup), encoding='utf-8')

if __name__ == '__main__':
    apply(Path(__file__).resolve().parents[1])
