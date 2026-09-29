#!/usr/bin/env python3
"""Read-only release checks beyond the shared FirstPair artifact contract."""
from pathlib import Path
import json,zipfile,xml.etree.ElementTree as ET,posixpath,re,csv
from urllib.parse import unquote,urlsplit
root=Path(__file__).resolve().parents[1];dist=root/'dist';errors=[]
data=json.loads((root/'presets.json').read_text());html=(root/'tutorial.html').read_text();man=(root/'manuscript.md').read_text()
for banned in ['switch toward capsule','rear HF switch','HF circuit IN','factory flat state']:
 if banned in html:errors.append('stale unsafe tutorial value: '+banned)
assert len(data['mics'])==2 and len(data['presets'])==3
assert data['mics'][0]['modes'][0].startswith('As found') and len(data['mics'][0]['modes'])==5
for path in set(re.findall(r'!\[[^\]]*\]\((assets/[^)]+)\)',man)):
 if not (root/path).is_file():errors.append('missing manuscript image '+path)
with zipfile.ZipFile(dist/'professional-podcat-audio.epub') as z:
 names=set(z.namelist());assert z.read('mimetype')==b'application/epub+zip'
 docs={n:ET.fromstring(z.read(n)) for n in names if n.endswith(('.xhtml','.opf','.ncx','.xml'))}
 for n,tree in docs.items():
  for e in tree.iter():
   for attr in ['src','href']:
    v=e.attrib.get(attr)
    if not v or urlsplit(v).scheme or v.startswith('#'):continue
    target=posixpath.normpath(posixpath.join(posixpath.dirname(n),unquote(urlsplit(v).path)))
    if target not in names:errors.append(f'{n}: missing {target}')
 cover=[e for n,t in docs.items() if n.endswith('.opf') for e in t.iter() if 'cover-image' in e.attrib.get('properties','').split()]
 if not cover:errors.append('no EPUB cover')
with (root/'comparison-log.csv').open() as f:fields=next(csv.reader(f))
with (root/'control-sweeps.csv').open() as f:sweeps=list(csv.DictReader(f))
assert len(fields)>=50 and len(sweeps)>=30
if (dist/'tutorial.html').read_bytes()!=(root/'tutorial.html').read_bytes():errors.append('dist tutorial differs from source')
report={'passed':not errors,'chapters':len(re.findall(r'^# ',man,re.M)),'wordCount':len(man.split()),'figures':len(re.findall(r'^!\[',man,re.M)),'recallFields':len(fields),'controlSweeps':len(sweeps),'epubFiles':len(names),'errors':errors}
print(json.dumps(report,indent=2));raise SystemExit(bool(errors))
