def foobar(x,y):
    return x + y + 42

a = 3
print(foobar(a+3,5))

def foobar1(x=1,y=0):
    return x + y + 42

print(foobar1(a+3,5))
print(foobar1(a+3))
print(foobar1())
print(foobar1(y=5))
