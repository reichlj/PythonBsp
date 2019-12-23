import matplotlib.pyplot as plt
import numpy as np

np.random.seed(34556)
gaussian_numbers = np.random.normal(size=10000)

#plt.hist(gaussian_numbers)
n, bin, patches = plt.hist(gaussian_numbers,bins=100)
plt.title('Gaussian Histogram')
plt.xlabel('Wert')
plt.ylabel('Häufigkeit')
plt.show()
print('bins:', bin)
print('n:', n)
print('patches', patches)
for i in range(len(patches)):
    print(patches[i])
