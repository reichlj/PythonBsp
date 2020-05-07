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
             columns=['population','area','density'],
             index=cities['name'])

city_frame['density'] = city_frame['population']/city_frame['area']

fig, ax = plt.subplots()
fig.suptitle('City Statistics')
ax.set_ylabel('Population')
ax.set_xlabel('Cities')

ax_area, ax_density = ax.twinx(), ax.twinx()
ax_area.set_ylabel('Area')
ax_density.set_ylabel('Density')

rspine = ax_density.spines['right']
rspine.set_position(('axes',1.25))
ax_density.set_frame_on(True)
ax_density.patch.set_visible(False)
fig.subplots_adjust(right=0.75)


city_frame['population'].plot(ax=ax,
                              style='b-',
                              use_index=True,rot=90)

ax2 = ax1.twinx()
city_frame['area'].plot(ax=ax_area,
                        style='g-',
                        use_index=True, 
                        rot=90)
city_frame['density'].plot(ax=ax_density,
                        style='r-',
                        use_index=True, 
                        rot=90)
