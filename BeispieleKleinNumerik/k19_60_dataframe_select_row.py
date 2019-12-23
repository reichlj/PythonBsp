import pandas as pd

cities = { 'name': ['London','Berlin','Madrid','Rome','Paris','Munich','Hamburg'],
           'population' : [8615246,3562166,3165235,2874038,2273305,1493900,1760433],
           'country' : ['England','Germany','Spain','Italy','France','Germany','Germany'] }

city_frame = pd.DataFrame(cities,columns=['name','population'],index=cities['country'])
print(city_frame)

print(city_frame.loc['Germany'])
print(city_frame.loc[['Germany','France']])
print(city_frame.loc[city_frame.population >2000000])