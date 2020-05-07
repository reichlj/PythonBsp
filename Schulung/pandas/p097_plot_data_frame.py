import pandas as pd

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
city_frame['area']*=1000
print(city_frame)
city_frame.plot()