import re
from collections import Counter

def word_freq(txt):
    word_dict = {}
    list_of_words = re.findall(r"\b\w+\b", txt)
    for word in list_of_words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1           
    items = list(word_dict.items())
    items.sort(key = lambda x: x[1], reverse=True)
    return items

def word_freq2(txt):
    word_dict = Counter()
    list_of_words = re.findall(r"\b\w+\b", txt)
    for word in list_of_words:
        word_dict[word] += 1
    return word_dict.most_common()

def word_freq3(txt):
    return Counter(re.findall(r"\b\w+\b", txt)).most_common()


fobj = open("data/1984.txt")
text = fobj.read()
fobj.close()
x = word_freq2(text)
print(x[:40])
x = word_freq3(text)
print(x[:40])
y = word_freq(text)
print(y)
