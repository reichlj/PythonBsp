import sys

print('*** sys.path ***')
for name in sys.path:
    print('->'+name+'<-')
print('*** end of sys.path ***')

import numpy
print('*** numpy ***')
print(numpy)
print('*** numpy.__file__ ***')
print(numpy.__file__)
print('*** dir(numpy) ***')
print(dir(numpy))
print('*** end of dir(numpy) ***')
