import numpy as np
import time
import timeit

size_of_vec = 1000000

def pure_python_version():
    t1 = time.time()
    x = range(size_of_vec)
    y = range(size_of_vec)
    z = [x[i]+y[i] for i in range(size_of_vec)]
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    x = np.arange(size_of_vec)
    y = np.arange(size_of_vec)
    z = x + y
    return time.time() - t1

t1 = pure_python_version()
t2 = numpy_version()
if t2 != 0:
    print('python={0:.6f} np={1:.6f} verhältnis={2:.3f}'.format(t1, t2, t1/t2))
else:
    print('python={0:.6f}'.format(t1))

timer1_obj = timeit.Timer("pure_python_version()",
                          "from __main__ import pure_python_version")
timer2_obj = timeit.Timer("numpy_version()",
                          "from __main__ import numpy_version")
t1 = timer1_obj.timeit(10)
t2 = timer2_obj.timeit(10)
print('python={0:.6f} np={1:.6f} verhältnis={2:.3f}'.format(t1, t2, t1/t2))

t1 = np.array(timer1_obj.repeat(repeat=5, number=10))
t2 = np.array(timer2_obj.repeat(repeat=5, number=10))
print(t1/t2)
