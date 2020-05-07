import re


text ='Hallo hallo abe abbbbe abce  abcdefuk aeb aebou  ae aeiou xae xaye xaeiou'
reg_ex = r'\b([^aeiou]*)([aeiou])([^aeiou]*)([aeiou])'
replace = r'\1\4\3\2'

res = re.sub(reg_ex, replace, text)
print(text)
print(res)

text = 'Es war einmal ein Mann, in dessen Haus wohnte eine Schlange,\n'+\
       'die wurde von dem Weibe dieses Mannes wohl gehalten und bekam \n'+\
       'täglich ihre Nahrung.'
res = re.sub(reg_ex, replace, text)
print(text)
print(res)


fh = open('der_mann_und_die_schlange.txt')
text = fh.read()
res = re.sub(reg_ex, replace, text)
print(text)
print(res)
