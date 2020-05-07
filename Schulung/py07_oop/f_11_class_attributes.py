class A:
    a = 'I am a class attribute'
    
x = A()
y = A()

print('x.a:',x.a)
print('y.a:',y.a)
print('A.a:',A.a)

x.a = 'new instance attribute for x!'
print('y.a:',y.a)
print('A.a:',A.a)
print('x.a:',x.a)

A.a = 'new class attribute'

print('y.a:',y.a)
print('A.a:',A.a)
print('x.a:',x.a)
