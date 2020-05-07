class Robot:
    pass

x = Robot()
y = Robot()

x.name = 'Marvin'
x.build_year = '1979'

y.name = 'Caliban'
y.build_year = '1993'
print(x.name)
print(y.build_year)

print(x.__dict__)
print(y.__dict__)

del y.build_year
print(y.__dict__)

y.__dict__['mein_name'] ='007'
print(y.__dict__)
print(y.mein_name)
