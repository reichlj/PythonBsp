
print("***   def f1(a=17, b='hall0')   ***")
def f1(a=17, b='hall0'):
    """Funktion f1"""
    print('f1 locals: ', locals())
    print('  a:', a, 'b:', b)

print(f1.__doc__)
f1(18, 'hall1')
f1(b=28, a='hall2')
f1(b='hall3')

print('***   def f2(a, *x)   ***')
def f2(a, *x):
    print('f2 locals: ', locals())
    print('  a:', a, type(a), 'x:', x, type(x))

f2(12, 34, 35)
t = (101, 102, 103, 104)
d = { 'z': 'eins', 'b': 102, 'c': 103, 'd': 105 }
print('*****f2-tupel')
f2(t)  # t an a
f2(*t) # erstes element von t an a; rest an x
print('*****f2-dictionary')
f2(d)  # d an a
f2(*d) # erster key von d an a, restliche keys an x

print('***   def f3(a, *x, **y)   ***')
def f3(a, *x, **y):
    print('f3 locals: ', locals())
    print('  a:', a, type(a), 'x:', x, type(x), 'y:', y, type(y))

t = (11, 12, 13, 14)
d = { 'z': 'eins', 'b': 12, 'c': 13, 'd': 14 }
f3(37, *t, **d)
f3(37, *t)
f3(37, **d)
d = { 'a': 'eins', 'b': 12, 'c': 13, 'd': 14 }
f3(**d)

print('***   def f4(a, **y)   ***')
def f4(a, **y):
    print('f4 locals: ', locals())
    print('  a:', a, type(a), 'y:', y, type(y))

d = { 'z': 'eins', 'b': 12, 'c': 13, 'd': 14 }
f4(5, **d)
d = { 'z': 'eins', 'a': 12, 'c': 13, 'd': 14 }
#f4(5, **d) # Fehler a ist zweimal definiert
f4(**d)
