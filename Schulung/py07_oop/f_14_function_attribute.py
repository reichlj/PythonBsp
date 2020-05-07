def f(x):
    f.counter = getattr(f,'counter',0) +1
    return 'Monty Python'

print(f.__dict__)
for i in range(10):
    f(i)

print(f.__dict__)
print(f.counter)
print(dir(f))