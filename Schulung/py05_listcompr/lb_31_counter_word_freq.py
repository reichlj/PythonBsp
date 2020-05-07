import re
from collections import Counter

def word_frequency(text):
    w_dict = Counter()
    words = re.findall(r'\b\w+\b',text.lower()) 
    for word in words:
        w_dict[word] +=1
    return w_dict.most_common()

fobj = open('1984.txt')
text = fobj.read()
fobj.close()
word_fre = word_frequency(text)
for element in word_fre[:20]:
    print(element)