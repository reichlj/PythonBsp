def f(x):
    try:
        z = 10/x
        return z
    except ZeroDivisionError as e:
        print('F: Some fix in f:',e)
        raise
        
try:
    y = 0
    iy = f(y)
except ZeroDivisionError as e:
    print('Main: Fixing the exception in main:',e)
    
print('Main: Program continues')
        