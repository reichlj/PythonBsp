def findnth(s,sub,n):
    num = 0
    start = -1
    while num < n:
        start = s.find(sub,start+1)
        if start == -1:
            break # return -1
        num +=1
    return start

def replacenth(source,search, replacement,n):
    pos = findnth(source,search,n)
    if pos == -1:
       return source
    return source[:pos] + replacement + source[pos+len(search):]

    
s = 'abcxyzabcjkjkjkabclkjkjlkjabcjlj'
print(replacenth(s,'abc','---',1))
print(replacenth(s,'abc','---',2))
print(replacenth(s,'abc','---',3))
print(replacenth(s,'abc','---',4))
print(replacenth(s,'abc','---',5))
    