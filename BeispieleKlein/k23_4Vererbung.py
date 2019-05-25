class A:
    def __init__(self):
        self.content = 42
        print('__init__ von A ausgeführt')

    def m(self):
        print('m von A ausgeführt')

class B(A):
    pass

if __name__ == '__main__':
    x = A()
    x.m()
    print('x.content=',x.content )
    print(x.__dict__)

    y = B()
    y.m()
    print('y.content=',y.content )
    print(y.__dict__)
