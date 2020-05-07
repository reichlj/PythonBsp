def letter_frequency(s):
    frequency_dict = {}
    for char in s.lower():
        if char.isalpha():
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    #f =  frequency_dict.items()      # Python2
    f =  list(frequency_dict.items()) # Python3
    f.sort(key = lambda x: (-x[1], x[0]))
    return f
s = "Monty Python"
x = letter_frequency(s)
print(x)
