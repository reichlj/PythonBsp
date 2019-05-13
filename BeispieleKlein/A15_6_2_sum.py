def summe(n):
    if n > 1:
        return n + summe(n - 1)
    else:
        return 1

print('s(1): ', summe(1))
print('s(2): ', summe(2))
print('s(3): ', summe(3))
print('s(4): ', summe(4))
