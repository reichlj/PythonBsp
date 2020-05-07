def f():
    s = 'cat'
    print(s)

def f1():
    global x
    x = 42

    
f()
#print(s)

f1()
print(x)