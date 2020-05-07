import matplotlib.pyplot as plt

X = [2, 4, 6,  8, 10]
Y = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(X,Y)

ax.set(xlabel='X values',
       ylabel='Y values',
       title='A Simple Graph')

ax.grid()
fig.savefig("simple_graph.png")
plt.show()
