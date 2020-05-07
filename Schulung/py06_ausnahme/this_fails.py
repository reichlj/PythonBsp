def this_fails():
    x = 1/0
    
try:
    this_fails()
except ZeroDivisionError as err:    
    print(type(err))
    print(print(err))
    print(print(err.args))
    print('Handling run-time error:', err)
    