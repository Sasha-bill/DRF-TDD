import requests
from lxml import html
from collections import Counter
import json

url = 'https://github.com/Sasha-bill/DRF-TDD'
page = requests.get(url)
tree = html.fromstring(page.content)

all_elms = tree.cssselect('*')
all_tags = [x.tag for x in all_elms]

c = Counter(all_tags)

print('all:', len(all_elms), 'span:', c['span'])

d = {}
for e in c:
    d[e] = c[e]

j = json.dumps(d, sort_keys=True, indent=4)
print(j)

