class A(object):
    def m(self):
        print('m in A')
    
class B(A):
    pass

class C(A):
    def m(self):
        A.m(self)
        super().m()
        print('m in C')

class D(B,C):
    pass

c = C()
c.m()
