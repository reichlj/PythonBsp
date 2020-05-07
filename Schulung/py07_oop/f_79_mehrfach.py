class A(): pass
class B1(A): pass
class B2(A): pass
class B3(A): pass
class B4(A): pass
class B5(A): pass
class C1(B1, B2, B3): pass
class C2(B4, B2, B5): pass
class C3(B4, B1): pass
class D(C1, C2, C3): pass


tpl = D.__mro__
for item in tpl:
    print(item)
