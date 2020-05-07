def nfind(haystack, needle, n, pos=0):
    pos = haystack.find(needle, pos)
    if n == 1 or pos == -1:
        return pos
    else:
        return nfind(haystack, needle, n-1, pos+1)


for i in range(7):
    print(i,nfind("abcjjjabcooiabckkabc", "c", i))
