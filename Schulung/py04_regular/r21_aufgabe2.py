import re

print('** x(xy)*x **')
for str in ['xx', 'xyxyxyx', 'xxyxy', 'xyxx', 'xxyxyx']:
    x = re.search(r'x(xy)*x', str)
    if x:
        print('match:', str, x.group())
    else:
        print('no match',str )

print('** x(xy)*x? **')
for str in ['xx', 'xyxyxyx', 'xxyxy', 'xyxx', 'xxyxyx']:
    x = re.search(r'x(xy)*x?', str)
    if x:
        print('match:', str, x.group(),x.span())
    else:
        print('no match',str )
