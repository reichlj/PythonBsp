import re

lst = ['20500-0001','20500-0002','20500']
reg_ex = r'(\d{5}|\d{5}-\d{4})'
reg_ex1 = r'(\d{5}-\d{4}|\d{5})'

for element in lst:
    ma = re.match(reg_ex,element)
    if ma:
        print(element,':', ma.group())
    else:
        print(element,':', ma)

for element in lst:
    ma = re.match(reg_ex1,element)
    if ma:
        print(element,':', ma.group())
    else:
        print(element,':', ma)