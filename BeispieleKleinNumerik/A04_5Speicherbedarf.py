import numpy as np
import sys
x = 1000
npx = np.array([x], dtype=np.int64)
print(x, 'size :', sys.getsizeof(x), x)
print(x, 'size :', sys.getsizeof(npx), npx[0])
x = 1000**10
print(x, 'size : ', sys.getsizeof(x))
try:
    npx = np.array([x], dtype=np.int64)
    print(x, 'size :', sys.getsizeof(npx), npx[0])
except OverflowError as e:
    print('Fehler:', e)

a = np.array([30,40,50])
print(type(a))
print(type(a[1]))
