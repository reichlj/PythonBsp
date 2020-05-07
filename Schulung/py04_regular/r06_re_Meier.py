import re
str = "Mayer ist nicht gleich Meier"
x = re.search(r"m..er",str)
print(x)
x = re.search("m..er",str)
print(x)
x = re.search(r"M..er",str)
print(x)
x = re.search("M..er",str)
print(x)
