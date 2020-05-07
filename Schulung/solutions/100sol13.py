def replacenth(source, search, replacement, n):
    pos = findnth(source, search, n)
    if pos == -1: 
        return source
    return source[:pos] + replacement + source[pos+len(search):]

s = "abcxyzabcjkjkjkabclkjkjlkjabcjlj"
print(findnth(s,"abc", 4))
print(replacenth(s,"abc","---", 4))
