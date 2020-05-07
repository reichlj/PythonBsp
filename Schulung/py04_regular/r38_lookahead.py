import re

x ='The man man man came down'
x ='The man man came down'
reg_ex = r'\b(\w+) (?=\1\b)'
replace = r''
print(re.sub(reg_ex,replace,x))

x ='The man man man came down'
x ='The man man came down'
reg_ex = r'\b(\w+) (?=\1\b)'
replace = r'xx'
print(re.sub(reg_ex,replace,x))
