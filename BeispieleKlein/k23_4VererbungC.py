class A:
    def __init__(self):
        self.contentA = 42
        print('__init__ von A ausgeführt')

    def m(self):
        print('m von A ausgeführt')

class B(A):
    def __init__(self):
        # A.__init__(self)
        super().__init__()
        self.contentB = 43
        print('__init__ von B ausgeführt')

    def m(self):
        print('m von B ausgeführt')
    pass

if __name__ == '__main__':
    x = A()
    x.m()
    print('x.contentA=', x.contentA)
    print('x.__dict__ =', x.__dict__)
    y = B()
    y.m()
    print('y.contentA=', y.contentA)
    print('y.contentB=', y.contentB)
    print('y.__dict__ =', y.__dict__)
