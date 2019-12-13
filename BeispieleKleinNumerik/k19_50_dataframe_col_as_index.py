import pandas as pd

cities = { 'name': ['London','Berlin','Madrid','Rome','Paris'],
           'population' : [8615246,3562166,3165235,2874038,2273305],
           'country' : ['England','Germany','Spain','Italy','France'] }
city_frame = pd.DataFrame(cities,columns=['name','population'],index=cities['country'])
print(city_frame)

city_frame = pd.DataFrame(cities)
city_frame2 = city_frame.set_index('country')
print(city_frame2)
