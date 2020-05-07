import re

def word_frequency(text):
    w_dict = {}
    words = re.findall(r'\b\w+\b',text.lower()) 
    for word in words:
        if word in w_dict:
            w_dict[word] +=1
        else:
            w_dict[word] = 1
    word_fre = list(w_dict.items())
    word_fre.sort(key=lambda item: (item[1], item[0]),reverse=True)
    return word_fre

fobj = open('1984.txt')
text = fobj.read()
fobj.close()
word_fre = word_frequency(text)
for element in word_fre[:20]:
    print(element)