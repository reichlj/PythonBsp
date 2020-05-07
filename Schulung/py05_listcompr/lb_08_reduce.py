import functools

x = [47,11,42,13]
print(functools.reduce(lambda x,y: x+y,x))

print(functools.reduce(lambda x,y: x+y,range(1,101)))

print(functools.reduce(lambda x,y: x*y,range(1,10)))

x = [47,11,42,102,13]
print(functools.reduce(lambda x,y: x if x>y else y,x))
    