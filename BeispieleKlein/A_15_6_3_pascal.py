def pascal(n, k):
    if n == 1:
        return 1
    elif k == 1 or k == n:
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)


print('pascal({},{})={}'.format(1, 1, pascal(1, 1)))
print('pascal({},{})={}'.format(2, 1, pascal(2, 1)))
print('pascal({},{})={}'.format(2, 2, pascal(2, 2)))
print('pascal({},{})={}'.format(3, 1, pascal(3, 1)))
print('pascal({},{})={}'.format(3, 2, pascal(3, 2)))
print('pascal({},{})={}'.format(3, 3, pascal(3, 3)))
print('pascal({},{})={}'.format(4, 1, pascal(4, 1)))
print('pascal({},{})={}'.format(4, 2, pascal(4, 2)))
print('pascal({},{})={}'.format(4, 3, pascal(4, 3)))
print('pascal({},{})={}'.format(4, 4, pascal(4, 4)))
print('pascal({},{})={}'.format(6, 1, pascal(6, 1)))
print('pascal({},{})={}'.format(6, 2, pascal(6, 2)))
print('pascal({},{})={}'.format(6, 3, pascal(6, 3)))
print('pascal({},{})={}'.format(6, 4, pascal(6, 4)))
print('pascal({},{})={}'.format(6, 5, pascal(6, 5)))
print('pascal({},{})={}'.format(6, 6, pascal(6, 6)))
