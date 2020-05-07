char_morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.','H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'...--', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', ';':'-.-.-', ':':'---...', '/':'-..-.', '-':'-....-', '\'':'.----.', '(':'-.--.-', ')':'-.--.-', '[':'-.--.-', ']':'-.--.-', '{':'-.--.-', '}':'-.--.-', '_':'..--.-'}

morse_char = {}
for char in char_morse:
    morse_char[char_morse[char]] = char
    
def txt2morse(txt, alphabet):
    morse_code = ""
    for char in txt.upper():
        if char == " ":
            morse_code += "   "
        else:
            morse_code += alphabet[char] + " "
    return morse_code

def morse2txt(txt, alphabet):
    res = ""
    mwords = txt.split("   ")
    for mword in mwords:
        for mchar in mword.split():
            res += alphabet[mchar]
        res += " "
    return res

mstring = txt2morse("So what?", char_morse)
print(mstring)
print(morse2txt(mstring, morse_char))
