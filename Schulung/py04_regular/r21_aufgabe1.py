import re
reg_exp_list = [
        r'ab+c?',   
        r'a?b*c',   
        r'b+c*',  
        r'^b+c*$',
        r'a.+b?c', 
        r'b{2,}c?', 
        r'^a{1,2}b+.?d*']

for str in ['abc', 'ac','abbb','bbc','aabcd','b']:
    print('**** '+ str + '****')
    for reg_exp in reg_exp_list:
        x = re.search(reg_exp,str)
        if x:
            print('match:',x.group())
        else:
            print('no match')
