import re
str = "Mayer ist nicht gleich Meier"
x = re.search(r"m..er",str)
print(x)
x = re.search(r"m..er",str,re.IGNORECASE)
print(x)
