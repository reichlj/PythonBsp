def f(a, b, x, y):
    print(a,b,x,y)
    
d = {'a':'append', 'b':'block', 'x':'extract', 'y':'yes'}

f(**d)

t = (47,11)
d = {'x':'extract', 'y':'yes'}
f(*t,**d)

d = {'a':'append', 'b':'block', 'x':'extract', 'y':'yes'}
f(*t,**d)
