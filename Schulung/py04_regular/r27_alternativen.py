import re

s = 'abcdef'
r = re.search('(abc|abcd)',s)
print(r.group())
r = re.search('(abcd|abc)',s)
print(r.group())
s = 'abcxdef'
r = re.search('(abcd|abc)',s)
print(r.group())


s = 'abcdef'
r = re.search('abcd?',s)
print(r.group())
