def f3(k):
    y1 = k
    y2 = 2*k
    y3 = 3*k
    return y1, y2, y3


def f4(k):
    y1 = k
    y2 = 2*k
    y3 = 3*k
    return (y1, y2, y3)


if __name__ == "__main__":
    x1, x2, x3 = f3(5)
    print('x1={0} x2={1} x3={2}'.format(x1, x2, x3))
    x = f3(6)
    print('x={0}'.format(x))
    y1, y2, y3 = f4(10)
    print('y1={0} y2={1} y3={2}'.format(y1, y2, y3))
    y = f4(11)
    print('y={0}'.format(y))
    z = 2, 3
    print('z={0}'.format(z))
