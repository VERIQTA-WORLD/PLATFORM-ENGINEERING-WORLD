"""Offline numbering, catalog, syntax, navigation and public-content checks."""
import ast
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
errors=[]
items=json.loads((ROOT/'02-course-catalog.json').read_text())['lessons']
if len(items)!=62:errors.append('catalog must contain 62 authored lessons')
if len({i['phase'] for i in items})!=25:errors.append('catalog must contain 25 phases')
ids=set()
for item in items:
    if item['id'] in ids:errors.append('duplicate lesson ID '+item['id'])
    ids.add(item['id'])
    p=ROOT/item['path']
    if not p.is_file():errors.append('missing lesson '+item['path']);continue
    body=p.read_text()
    if len(body.split())<300:errors.append(item['path']+': review lesson depth')
    if '## ' not in body:errors.append(item['path']+': missing teaching sections')
for path in ROOT.rglob('*'):
    relative=path.relative_to(ROOT)
    if any(part in ('.git','__pycache__') for part in relative.parts):continue
    if not re.match(r'^\d{2}-',path.name):errors.append('unnumbered path '+relative.as_posix())
    if not path.is_file():continue
    try:
        if path.suffix=='.py':ast.parse(path.read_text(),filename=str(relative))
        if path.suffix=='.json':json.loads(path.read_text())
        if path.suffix=='.svg':ET.fromstring(path.read_text())
    except (SyntaxError,ValueError,ET.ParseError) as error:errors.append(str(relative)+': '+str(error))
    if path.suffix not in ('.md','.json','.svg','.yaml','.yml','.txt'):continue
    body=path.read_text()
    for pattern in (r'/Users/[A-Za-z]',r'AKIA[0-9A-Z]{16}',r'gh[pousr]_[A-Za-z0-9]{30,}',r'-----BEGIN .*PRIVATE KEY-----'):
        if re.search(pattern,body):errors.append(str(relative)+': possible private content')
    if path.suffix=='.md':
        for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)',body):
            target=match.group(1).split('#')[0].split(' "')[0]
            if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:',target):continue
            if not (path.parent/unquote(target)).exists():errors.append(str(relative)+': broken local link '+target)
        for target in re.findall(r'<img[^>]+src="([^"]+)"',body):
            if not target.startswith('http') and not (path.parent/target).is_file():errors.append('missing image '+target)
if errors:
    print('\n'.join(errors));sys.exit(1)
print('PASS: 62 lessons, 25 phases, numbered paths, local links, Python/JSON/SVG syntax and public-content pattern checks')
