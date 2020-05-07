import pandas as pd

cities = { 'name': ['London','Berlin','Madrid',
                    'Rome','Paris','Vienna'],
    'population' : [8615246,3562166,3165235,
                    2874038,2273305,1805681],
    'country'    : ['England','Germany','Spain',
                    'Italy','France','Austria'] }

city_frame = pd.DataFrame(cities)
city_frame2 = city_frame.set_index('country')
print(city_frame2)
print('-------------------------------')
city_frame = pd.DataFrame(cities)
city_frame.set_index('country',inplace=True)
print(city_frame)
