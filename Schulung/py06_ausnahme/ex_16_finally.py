try:
    x = float(input('Your number: '))
    inverse = 1.0/x
finally:
    print('There may or may not have been an exception.')

print('The inverse: ',inverse)