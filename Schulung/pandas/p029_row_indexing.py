import pandas as pd

cities = { 'name': ['London','Berlin','Madrid',
                    'Rome','Paris','Vienna','Munich','Hamburg'],
    'population' : [8615246,3562166,3165235,
                    2874038,2273305,1805681,1493900,1760433],
    'country'    : ['England','Germany','Spain',
                    'Italy','France','Austria','Germany','Germany'] }

city_frame = pd.DataFrame(cities,columns=['name','population'],
                                 index=cities['country'])
print(city_frame)

print(city_frame.loc[city_frame.population>2000000])

cond1 = city_frame.population>1500000
cond2 = city_frame['name'].str.contains('m')
print(city_frame.loc[cond1 & cond2])
print(city_frame.iloc[[0,2,5]])


