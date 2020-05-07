def fib(n):
    a, b = 0, 1
    for k in range(n):
        a,b = b, a+b
    return a

def fiblist(n):
    fib = [0,1]
    for k in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib