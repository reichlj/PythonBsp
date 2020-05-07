class A:
    def __init__(self):
        print('Init von Y')

    def __call__(self,*args,**kwargs):
        print('Argumente lauten',args,kwargs)

x = A()
print(id(x))
x(3,4,x=11,y=12)
print(id(x))
y = A.__call__(4,5,x=21,y=22)
print(id(y))
