import re
re.purge()
p = re.compile("(ab)*")
mystr = 'ababababab'
print('****',mystr)
print(p.search(mystr).span())
print(p.search(mystr).group())
print(p.search(mystr).groups())

p = re.compile("(ab)*")
mystr = 'xyababababab'
print('****',mystr)
print(p.search(mystr).span())
for count,item in enumerate(p.finditer(mystr)):
    print(count, ':', item.span(),' : ', item.group())

p = re.compile("[ab]+")
mystr = 'xyababababab'
print('****',mystr)
print(p.search(mystr).span())
print(p.search(mystr).group())

p = re.compile("[ab]*")
mystr = 'xyababababab'
print('****',mystr)
print(p.search(mystr).span())
for count,item in enumerate(p.finditer(mystr)):
    print(count, ':', item.span(),' : ', item.group())

p = re.compile("[ab]*")
mystr = 'abababababxy'
print('****',mystr)
print(p.search(mystr).span())

m = re.match("([abc])+", "abc")
print(m.groups())
