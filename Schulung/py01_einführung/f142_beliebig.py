def beliebig(x, y, *mehr):
    print('x=',x,'y=',y)
    print('*mehr',mehr)

beliebig(3,4)
beliebig(3,4,'Hallo Welt',3,4)

def f(x,y,*z):
    s = x + y
    for k in z:
        s += k
    return s

print(f(1,2))
print(f(1,2,4,5))
tp = (4,5,6)
print( f(1,2, *tp) )
print( f(1,2, *range(3,101)) )
print( f(1,2, *list(range(3,101))) )
print( f(*range(1,101)) )
