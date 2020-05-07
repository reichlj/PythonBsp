def fak(n):
    if n == 1:
        return 1
    if n>1:
        return n*fak(n-1)
    
print(fak(4))
