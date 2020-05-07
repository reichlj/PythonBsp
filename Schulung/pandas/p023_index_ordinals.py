import pandas as pd

cities = { 'name': ['London','Berlin','Madrid',
                    'Rome','Paris','Vienna'],
    'population' : [8615246,3562166,3165235,
                    2874038,2273305,1805681],
    'country'    : ['England','Germany','Spain',
                    'Italy','France','Austria'] }

ordinals = ["first","second","third","fourth","fifth",'sixth']

city_frame = pd.DataFrame(cities,ordinals)
print(city_frame)

print('-------------------------')
city_frame = pd.DataFrame(cities)
city_frame.index = ordinals
print(city_frame)