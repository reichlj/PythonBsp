from collections import defaultdict 

def letter_frequency(s):
    letter_fre = defaultdict(lambda : 0)
    for letter in s.lower():
        if letter.isalpha():
            letter_fre[letter] += 1
    items = [ (c,round(f/len(s),4)) for c,f in letter_fre.items()]
    # items.sort(key=itemgetter(1,0),reverse=True)
    items.sort(key=lambda x: (-x[1], x[0]))
    return items

s = 'Monty Python'
x = letter_frequency(s)
for element in x:
    print(element)
    
print('1984.txt')
s = open('1984.txt').read()
x = letter_frequency(s)
for element in x:
    print(element)