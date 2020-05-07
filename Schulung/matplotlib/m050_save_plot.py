import matplotlib.pyplot as plt

fig = plt.figure()

X = [1,2,3,4,5,6,7]
Y = [1,3,4,2,5,8,6]

axes1 = fig.add_axes([0.1,0.1,0.9,0.85])
axes2 = fig.add_axes([0.2,0.6,0.4,0.2])

axes1.plot(X, Y,'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')

axes2.plot(Y,X,'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('title inside')
plt.tight_layout()
plt.show()

fig.savefig('m050_save.png')
fig.savefig('m050_save_dpi.png',dpi=200)