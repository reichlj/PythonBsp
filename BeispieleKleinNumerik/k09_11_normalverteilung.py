import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

n = 1000
values = []
frequencies = {}
while len(values) < n:
    value = int(rd.normal(180,30))
    if 130 < value < 230:
        frequencies[value] = frequencies.get(value,0) + 1
        values.append(value)
print(values[:7])

frequencies = dict.fromkeys(range(131,231),0)
k = 0
while k < n:
    value = int(rd.normal(180,30))
    if 130 < value < 230:
        frequencies[value] += 1
        k +=1
print(frequencies[180])

freq = list(frequencies.items()) # freq 99 Tupel mit je zwei Werten
freq.sort()

# list(zip(*freq))  Liste mit zwei Elementen, jedes Element ist ein Tupel mit 99 Elementen
# x,y = list(zip(*freq))
plt.plot(*list(zip(*freq)))
plt.show()