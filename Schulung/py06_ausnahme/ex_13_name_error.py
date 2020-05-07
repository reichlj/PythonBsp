try:
    raise NameError('Hi There')
except NameError:
    print('An exception flew by!')
    raise