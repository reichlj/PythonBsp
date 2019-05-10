def fib_intervall(x):
    if x < 0:
        return -1
    old, new = 0, 1
    while True:
        if new < x:
            old,new = new, old+new
        else:
            return (old, new)

for k in range(10):
    print(k,fib_intervall(k))

