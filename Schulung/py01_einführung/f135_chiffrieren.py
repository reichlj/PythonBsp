import string
from random import sample

def encrypt(text, edict):
    res = ""
    for char in text:
        #res = res + edict.get(char,char)
        res = res + edict.get(char)
    return res

alphabet = string.ascii_letters
print(alphabet)
#  sample(population, k) :     
#     Return a k length list of unique elements chosen from the  
#     population sequence. Used for random sampling without replacement.
permutated_alphabet = sample(alphabet, len(alphabet))
print(permutated_alphabet,'\n')

encrypt_dict = dict(zip(alphabet, permutated_alphabet))
decrypt_dict = dict(zip(permutated_alphabet, alphabet))

txt = """Windmills are the greatest 
threat in the US to both bald
and golden eagles. Media claims
fictional 'global warming' is worse."""

ctext = encrypt(txt, encrypt_dict)
print(ctext+'\n')
print(encrypt(ctext, decrypt_dict))
