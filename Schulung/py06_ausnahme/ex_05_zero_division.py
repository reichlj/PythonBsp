numbers = [3.7832, 8.5, 0, 1.9]
for x in numbers:
    print(x, end=' ')
    try:
        print(1.0/x)
    except ZeroDivisionError:
        print('** no inverse **')
