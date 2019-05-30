h = int(input('Stunde: '))
m = int(input('Minute: '))
s = int(input('Sekunde: '))
print('Uhrzeit: {0:02d}:{1:02d}:{2:02d}'.format(h,m,s))
s = s + 1
if s == 60:
    s=0;
    m = m +1
    if m == 60:
        m = 0
        h = h + 1
print('Uhrzeit: {0:02d}:{1:02d}:{2:02d}'.format(h,m,s))
