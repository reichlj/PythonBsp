try:
    x = float(input('Your number: '))
    inverse = 1.0/x
except ValueError:
    print('Only an int or a float are possible')
except ZeroDivisionError:
    print('Infinity')
else:
    print('All\'s Well That Ends Well!')        
finally:
    print('There may or may not have been an exception.')