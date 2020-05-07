import matplotlib.pyplot as plt

fig, ax =plt.subplots(2,3,sharex='col',sharey='row')
for row in range(2):
    for col in range(3):
        ax[row][col].text(0.5,0.5, str((row,col)),
                      color='green',fontsize=18,ha='center')
plt.show()