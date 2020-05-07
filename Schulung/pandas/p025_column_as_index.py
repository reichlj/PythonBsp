import pandas as pd

cities = { 'name': ['London','Berlin','Madrid',
                    'Rome','Paris','Vienna'],
    'population' : [8615246,3562166,3165235,
                    2874038,2273305,1805681],
    'country'    : ['England','Germany','Spain',
                    'Italy','France','Austria'] }

city_frame = pd.DataFrame(cities,
            columns=['name','population'],
            index=cities['country'])

print(city_frame)
