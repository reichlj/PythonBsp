import re
s = "abcxyzkkbabcllkk"
x = re.search(r'^abc.*kk',s)
print(x.group())
x = re.search(r'^abc.*?kk',s)
print(x.group())
