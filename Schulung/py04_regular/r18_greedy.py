import re
str = "Meier/MAYER geht auch mit y"
mo = re.search(r"M[ea][iy]er",str)
print(mo)
print(mo.span())
print(mo.group())

mo = re.search(r"M[ea][iy]er",str,re.I)
print(mo.group())
mo = re.search(r"M[ea][iy]er",str[1:],re.I)
print(mo.group())
