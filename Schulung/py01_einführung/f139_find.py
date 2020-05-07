def findnth(s,sub,n):
    num = 0
    start = -1
    while num < n:
        start = s.find(sub,start+1)
        if start == -1:
            break # return -1
        num +=1
    return start

s = 'abcxyzabcjkjkjkabclkjkjlkjabcjlj'
print(findnth(s,'abc',1))
print(findnth(s,'abc',2))
print(findnth(s,'abc',3))
print(findnth(s,'abc',4))
print(findnth(s,'abc',5))
    