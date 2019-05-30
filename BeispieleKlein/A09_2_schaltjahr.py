jahr = int(input('Jahr: '))
if jahr%4 == 0:
    if jahr%400 == 0:
        print('Schaltjahr')
    elif jahr%100 == 0:
        print('Kein Schaltjahr')
    else:
        print('Schaltjahr')
else:
    print('Kein Schaltjahr')

if jahr%4 == 0 and jahr%100 != 0 or jahr%400 == 0:
    print('Schaltjahr')
else:
    print('Kein Schaltjahr')

