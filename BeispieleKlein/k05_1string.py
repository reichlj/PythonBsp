x=1
if x == 1:
    s1="abc \
        123 \
        def"
else:
    s1="ABc \
        def"
print(s1)

y=1
if y == 1:
    s2="""xyc 
         def"""
else:
    s2="""XYc 
        def"""
print(s2)
print(len(r'\n123'))
print(len('\n123'))

x=[1,2,3]
print(x[:2])
print(x[:])
print(x[2:2])
print(x[2:-1])
print(x[::-1])
print(x[::])

a=bytes([3,49,50,65,66])
print(a)

