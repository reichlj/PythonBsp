import re
str = "Mayer ist nicht gleich Meier"
x = re.search(r"M..er",str)
print(x.group())
print(x.start())
print(x.end())
print(x.span())
