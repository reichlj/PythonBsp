import pandas as pd
import matplotlib.pyplot as plt

cities = { 'name': ['London','Berlin','Madrid','Rome',
                    'Paris','Vienna'],
    'population' : [8615246,3562166,3165235,2874038,
                    2273305,1805681],
    'area'       : [1572,891.85,605.77,1285,105.4,414.6] }

city_frame = pd.DataFrame(cities,
             columns=['population','area'],
             index=cities['name'])

print(city_frame)

city_frame.plot(xticks=range(len(city_frame.index)),
                use_index=True,rot=90)

fig, ax = plt.subplots()
fig.suptitle('City Statistics')
ax.set_ylabel('Population')
ax.set_xlabel('Cities')

ax2 = ax.twinx()
ax2.set_ylabel('Area')

city_frame['population'].plot(ax=ax,
                              style='b-',
                              use_index=True, 
                              rot=90)
city_frame['area'].plot(ax=ax2,
                              style='g-',
                              use_index=True, 
                              rot=90)
