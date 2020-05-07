import pandas as pd

cities = { 'name': ['London','Berlin','Madrid',
                    'Rome','Paris','Vienna','Munich','Hamburg'],
    'population' : [8615246,3562166,3165235,
                    2874038,2273305,1805681,1493900,1760433],
    'country'    : ['England','Germany','Spain',
                    'Italy','France','Austria','Germany','Germany'] }

city_frame = pd.DataFrame(cities,index=cities['country'])
print(city_frame)
print(city_frame['population'].cumsum())

city_frame['population'] = [1,20,300,4000,50000,6,7,8]
print(city_frame)