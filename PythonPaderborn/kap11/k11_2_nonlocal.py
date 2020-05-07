def f():
    x = 1
    def g():
        print('f->g: ',x)
    g()

def f1():
    def g1():
        print('f1->g: ',x)
    x = 1
    g1()

def f2():
    def g2():
        nonlocal x
        x = 3
        print('f1->g: ',x)
    x=0
    g2()

f()
f1()
f2()
