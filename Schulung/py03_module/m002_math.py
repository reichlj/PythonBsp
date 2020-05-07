n = 1

if n == 1: 
    import math
    print(math)
    #print(math.__file__) #math has no __file__ attribute
    print('*** dir(math) ***')
    print(dir(math))
    print('*** dir() ***')
    print(dir())
elif n == 2:
    from math import sin, cos
    # print(math) # math not defined
    print('*** dir() ***')
    print(dir())
elif n == 3:
    from math import *
    #print(math) # math not defined
    print('*** dir() ***')
    print(dir())
elif n == 4:
    import math as m
    print(m)
    print('*** dir(m) ***')
    print(dir(m))
    print('*** dir() ***')
    print(dir())
