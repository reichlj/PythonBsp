import re

fobj = open('1984.txt')
count = 0
for line in fobj:
    # r = re.search(r'\b(\w+)\W\1\W',line) # 2 matches
    r = re.search(r'\b(\w+)\s\1\W',line)   # 1 match
    #r = re.search(r'\b(\w+)\1\b',line)   # 1 match
    if r:
        print('count=',count)
        print('->'+r.group()+'<-', line)
    count +=1
fobj.close()

r = re.search(r'\b(\w+)\s\1\b', "ab ab xy")
print(r)
r = re.search(r'\b(\w+)\s\1\b', "ab ab1 y")
print(r)