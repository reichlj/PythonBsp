import re

str = "yes I said yes I will Yes."
res = re.sub('[yY]es','no',str)
print(res)
