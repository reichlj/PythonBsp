import pandas as pd

cities = { 'name': ['London','Berlin','Madrid',
                    'Rome','Paris','Vienna','Munich','Hamburg'],
    'population' : [8615246,3562166,3165235,
                    2874038,2273305,1805681,1493900,1760433],
    'country'    : ['England','Germany','Spain',
                    'Italy','France','Austria','Germany','Germany'] }

city_frame = pd.DataFrame(cities,
            columns=['country','population','cum_population'],
            index=cities['name'])

city_frame['cum_population'] = city_frame['population'].cumsum()
print(city_frame)
