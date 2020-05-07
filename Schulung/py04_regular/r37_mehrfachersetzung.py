import re

x ='The man man man came down'
reg_ex = r'\b(\w+)\b\s\1'
replace = r'\1'
while re.search(reg_ex,x):
    x = re.sub(reg_ex,replace,x)
    print(x)
