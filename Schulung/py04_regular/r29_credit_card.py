import re

visa = r'4(\d{15}|\d{12})'
#master = r'(51|52|53|54|55)\d{13}4'
master = r'5[1-5]\d{13}4'
#diner = r'(30|36|38)\d{11}4'
diner = r'3[068]\d{11}4'
american = r'(34|37)\d{12}9'
discover = r'6011\d{11}4'

exprs = {'discover':discover, 'master':master, 'diner':diner,
         'american':american, 'visa':visa}

lst = [
       '4123123412341234',
       '5523123412341234',
       '30231234123434',
       '342312341234129',
       '6011123412341234',       
       '9911123412341234'       
       ]
for element in lst:
    for reg in exprs:
        mo = re.search(exprs[reg],element)
        if mo:
           print(element,':', reg)
           break
    else:
        print('No match for',element)
