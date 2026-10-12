import pathlib,sys,urllib.parse,json
ROOT=pathlib.Path(__file__).resolve().parents[1];coord=pathlib.Path(r'C:\Users\Admin\OneDrive - CWU\AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration');sys.path.insert(0,str(coord/'.deps'))
from bs4 import BeautifulSoup
errors=[];pages=list(ROOT.rglob('*.html'))
for p in pages:
    s=BeautifulSoup(p.read_text(encoding='utf8'),'html.parser')
    for tag in s.select('[href],[src]'):
        value=tag.get('href') or tag.get('src');u=urllib.parse.urlsplit(value)
        if u.scheme or not u.path:continue
        target=(p.parent/urllib.parse.unquote(u.path)).resolve()
        if not target.exists():errors.append({'page':str(p.relative_to(ROOT)),'missing':value})
    if s.select('script[src*="google"],iframe'):errors.append('Unexpected external tracking or embed')
print(json.dumps({'pages':len(pages),'errors':errors},indent=2));sys.exit(bool(errors))
