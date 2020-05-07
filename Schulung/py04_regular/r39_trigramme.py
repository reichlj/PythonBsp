import re

def trigram_frequency(lst_trigr):
    frequency_dict = {}
    for item in lst_trigr:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    f = [item for item in frequency_dict.items()]
    f.sort(key= lambda x: x[1], reverse=True) 
    return f       
    
text = open('river_snake.txt').read()
list_3grams = re.findall(r'(?=([A-Za-z]{3}))',text)
res= trigram_frequency(list_3grams)
print(res[:10])
