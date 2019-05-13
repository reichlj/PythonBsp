def f(n):
    if n > 1:
        return 3 + f(n-1)
    else:
        return 3

print('f(1): ', f(1))
print('f(2): ', f(2))
print('f(3): ', f(3))
print('f(4): ', f(4))
