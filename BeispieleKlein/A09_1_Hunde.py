alter = int(input('Alter: '))
ma = 0
if alter >= 1:
    ma = 14
if alter >= 2:
    ma = 22
if alter >= 3:
    ma = ma + 5*(alter-2)
print('Alter {0} entspricht Hundealter {1}\n'.format(alter,ma))
