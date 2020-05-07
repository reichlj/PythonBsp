def txt2Morse(txt, alphabet):
    mtxt= ""
    for c in txt.upper():
        if c == ' ':
            mtxt += '   '
        else:
            mtxt += alphabet[c] + ' '
    return mtxt
    

def morse2Txt(m, alphabet):
    txt = ''
    words = m.split('   ')
    for word in words: 
        for char in word.split():
            txt += alphabet[char]
        txt += ' '
    return txt

char_morse = {
    "A" : ".-",       "B" : "-...",     "C" : "-.-.",     "D" : "-..",
    "E" : ".",        "F" : "..-.",     "G" : "--.",      "H" : "....",
    "I" : "..",       "J" : ".---",     "K" : "-.-",      "L" : ".-..",
    "M" : "--",       "N" : "-.",       "O" : "---",      "P" : ".--.",
    "Q" : "--.-",     "R" : ".-.",      "S" : "...",      "T" : "-",
    "U" : "..-",      "V" : "...-",     "W" : ".--",      "X" : "-..-",
    "Y" : "-.--",     "Z" : "--..",     "0" : "-----",    "1" : ".----",
    "2" : "..---",    "3" : "...--",    "4" : "....-",    "5" : ".....",
    "6" : "-....",    "7" : "--...",    "8" : "---..",    "9" : "----.",
    "." : ".-.-.-",   "," : "--..--",   "?" : "..--..",   ";" : "-.-.-"
}    

morse_char = {}
for char in char_morse:
    morse_char[char_morse[char]] = char
    
text = 'So what?' 
print(text)   
mstring = txt2Morse(text,char_morse)
text1 = morse2Txt(mstring, morse_char)
print(text1)