import re
str = "Monty Python"
x = re.search(r"Python$",str)
print(x)
print(x.group())
