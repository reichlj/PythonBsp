from timeit import Timer
from k15_5memory import fibm

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)

def fibi(n):
    if n < 2:
        return n
    a, b = 0, 1
    for k in range(n-1):
        a, b = b, a + b
    return b
    # a, b = 0, 1
    # for k in range(n):
    #     a, b = b, a + b
    # return a


def test_fibonacci():
    for k in range(7):
        f, fi, fm = fib(k), fibi(k), fibm(k)
        if (f != fi) or (f != fm):
            print('Fehler: n={0}, fib={1} fibi={2} fibm={3}'.format(k, f, fi, fm))


if __name__ == '__main__':

    test_fibonacci()
    from_fib = "from k15_5Fibonacci import fib"
    from_fibi = "from k15_5Fibonacci import fibi"
    from_fibm = "from k15_5memory import fibm"

    for k in range(34):
        timer_fib = Timer("fib(" + str(k) + ")", from_fib)
        t_fib = timer_fib.timeit(3)
        timer_fibi = Timer("fibi(" + str(k) + ")", from_fibi)
        t_fibi = timer_fibi.timeit(3)
        print('k={0:2d} fib={1:9.6f} fibi{2:9.6f} quot={3:11.3f}'.format(
               k, t_fib, t_fibi, t_fib/t_fibi))

    for k in range(40):
        timer_fibi = Timer("fibi(" + str(k) + ")", from_fibi)
        t_fibi = timer_fibi.timeit(10)
        timer_fibm = Timer("fibm(" + str(k) + ")", from_fibm)
        t_fibm = timer_fibm.timeit(10)
        print('k={0:2d} fibm{1:9.6f} fibi{2:9.6f} quot={3:6.3f}'.format(
               k, t_fibm, t_fibi, t_fibm/t_fibi))
