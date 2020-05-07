from operator import itemgetter

def letter_frequency(s):
    letter_fre = {}
    for letter in s.lower():
        if not letter.isalpha():
            continue
        if letter in letter_fre:
            letter_fre[letter] += 1
        else:
            letter_fre[letter] = 1
    items = list(letter_fre.items())
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