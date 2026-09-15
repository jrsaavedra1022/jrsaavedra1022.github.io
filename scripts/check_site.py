"""Check published routes and local link/asset integrity without dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
ROOT=Path(__file__).resolve().parents[1]
class Document(HTMLParser):
 def __init__(self,text):
  super().__init__(); self.links=[]; self.ids=set();self.feed(text)
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if 'id' in attrs:self.ids.add(attrs['id'])
  for key in ('href','src'):
   if key in attrs:self.links.append(attrs[key])
errors=[]
files=list(ROOT.rglob('*.html'))
docs={p:Document(p.read_text()) for p in files}
for source,doc in docs.items():
 text=source.read_text()
 if 'REPLACE_WITH' in text:errors.append(f'{source}: unresolved placeholder')
 if '<title>' not in text or 'name="viewport"' not in text:errors.append(f'{source}: missing metadata')
 for link in doc.links:
  url=urlsplit(link)
  if url.scheme or url.netloc:continue
  target=(ROOT/unquote(url.path.lstrip('/')) if url.path.startswith('/') else source.parent/unquote(url.path)).resolve() if url.path else source
  if target.is_dir():target=target/'index.html'
  if not target.is_file():errors.append(f'{source.relative_to(ROOT)}: missing {link}')
  elif url.fragment and target in docs and unquote(url.fragment) not in docs[target].ids:errors.append(f'{source.relative_to(ROOT)}: missing anchor {link}')
for app in ('popora','snapclip','flappy-dragons','dragon-flip','dragon-flip/en'):
 for route in ('index.html','support/index.html','privacy/index.html'):
  if not (ROOT/'apps'/app/route).exists():errors.append(f'missing {app}/{route}')
 support=(ROOT/'apps'/app/'support/index.html').read_text()
 if 'mailto:popora.support@gmail.com' not in support:errors.append(f'{app}: support contact missing')
# All localized Dragon Flip pages and legacy destinations must exist.
for prefix in ('apps/dragon-flip', 'apps/dragon-flip/en'):
 for section in ('', 'support/', 'privacy/', 'terms/'):
  p=ROOT/prefix/section/'index.html'
  if not p.exists():errors.append(f'missing {p}')
  elif 'Dragon Flip' not in p.read_text():errors.append(f'{p}: wrong brand')
for section in ('', 'support/', 'privacy/'):
 old=(ROOT/'apps/flappy-dragons'/section/'index.html').read_text()
 if f'url=/apps/dragon-flip/{section}' not in old:errors.append(f'legacy route not mapped: {section}')
if re.search(r'http-equiv=["\']refresh', (ROOT/'index.html').read_text(),re.I):errors.append('root must be a real page')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(files)} HTML pages; local links/assets/anchors and required routes are valid.')
