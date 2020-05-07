import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
fig, ax =plt.subplots(1,2,sharex='col',sharey='row')

ax[0].text(0.5,0.5,'left',color='green',fontsize=18,ha='center')
ax[1].text(0.5,0.5,'right',color='green',fontsize=18,ha='center')

plt.show()