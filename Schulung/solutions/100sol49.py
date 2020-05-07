np.zeros(7)

checkerboard = np.zeros((8,8),dtype=int)
checkerboard[::2,1::2] = 1
checkerboard[1::2,::2] = 1
print(checkerboard)
#alternativ:
np.tile([[1,0],[0,1]],(4,4))
