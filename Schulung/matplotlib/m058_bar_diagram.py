import matplotlib.pyplot as plt
import numpy as np

plt.figure()
years = ('2010','2011','2012','2013','2014',
         '2015','2016','2017','2018')
visitors = (1241,50927,162242,222093,665004,
            2071987,2460407,3779970,5335831)

index = np.arange(len(visitors))
bar_width = 1.0
plt.bar(index,visitors,bar_width,color='green',align='center')

plt.xticks(index,years)
plt.show()
