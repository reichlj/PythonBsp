import re

fobj = open('war_and_peace.txt')
count = 0
for line in fobj:
    #r = re.search(r'\b(\w{6,})\b.*\1',line)
    r = re.search(r'\b(\w{6,}).*\b\1',line)
    if r:
        print('count=',count)
        print('->'+r.group()+'<-', line)
    count +=1
fobj.close()
#line = 'contact ccontact'
line = 'contact contact'
r = re.search(r'\b(\w{6,}).*\b\1\b', line)
if r:
    print('->' + r.group() + '<-')
