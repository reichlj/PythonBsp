import numpy as np
from io import StringIO
data = "1, abc , 2\n 3, xxx, 4"
a1 = np.genfromtxt(StringIO(data),delimiter=",",dtype="|U5")
a2 = np.genfromtxt(StringIO(data),delimiter=",",dtype="|U5",autostrip=True)

print(a1)
print(a2)

b1 = np.genfromtxt(StringIO(data),delimiter=",",dtype="|U1")
b2 = np.genfromtxt(StringIO(data),delimiter=",",dtype="|U1",autostrip=True)
print(b1)
print(b2)

