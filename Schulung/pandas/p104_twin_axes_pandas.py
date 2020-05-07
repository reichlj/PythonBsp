import pandas as pd
import matplotlib.pyplot as plt

cities = { 'name': ['London','Berlin','Madrid','Rome',
                    'Paris','Vienna','Bucharest','Hamburg',
                    'Budapest','Warsaw','Barcelona',
                    'Munich','Milan'],
    'population' : [8615246,3562166,3165235,2874038,
                    2273305,1805681,1803425,1760433,
                    1754000,1740119,1602386,
                    1493900,1350680],
    'area'       : [1572,891.85,605.77,1285,
                    105.4,414.6,228,755,
                    525.2,517,101.9,310.4,181.8] }
    
city_frame = pd.DataFrame(cities,
             columns=['population','area'],
             index=cities['name'])

print(city_frame)

ax1= city_frame['population'].plot(style='b-',
                  xticks=range(len(city_frame.index)),
                  use_index=True,rot=90)

ax2 = ax1.twinx()
city_frame['area'].plot(ax=ax2,
                        style='g-',
                        use_index=True, 
                        rot=90)

ax1.legend(loc=(.7,.9),frameon = False)
ax2.legend(loc=(.7,.85),frameon = False)

plt.show()