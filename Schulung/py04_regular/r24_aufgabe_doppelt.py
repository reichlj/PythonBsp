import re

print(re.search(r'([a-z][0-9])\s+\1','a4 a4'))
print(re.search(r'([a-z][0-9])\s+\1','a4 x2'))