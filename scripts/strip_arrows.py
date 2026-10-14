"""Remove link arrow glyphs and their empty icon wrappers after each rebuild."""
from pathlib import Path
import re
ARROWS=re.compile('[\u2190-\u21ff\u2794\u27a1]')
def apply(root):
 for file in Path(root).rglob('*.html'):
  text=file.read_text(encoding='utf8')
  text=re.sub(r'<(span|b)(?:\s[^>]*)?>\s*'+ARROWS.pattern+r'\s*</\1>','',text)
  text=ARROWS.sub('',text)
  file.write_text(text,encoding='utf8')
if __name__=='__main__':apply(Path(__file__).resolve().parents[1])
