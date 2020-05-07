import re


txt = 'Wohnort: 78224 Singen'
mo = re.search(r'\D([\d]{5})\D',txt)
print(mo.group(1))
mo = re.search(r'\D(\d{5})\D',txt)
print(mo.group(1))
c = re.compile(r'\D([\d]{5})\D')
m = c.search(txt)
print(m)