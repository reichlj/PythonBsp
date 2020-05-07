class X:
    pass

x = X()

try:
    print(x.energy)
except Exception as e:
    print(e)

print(getattr(x,'energy',100))  # attribute wird nicht erzeugt!
try:
    delattr(x, 'energy')
except Exception as e:
    print('exception bei delattr:', e)

setattr(x,'energy',101)
print(hasattr(x,'energy'))
print(getattr(x,'energy'))
print(x.__dict__)
delattr(x,'energy')
print('nach delattr', x.__dict__)
