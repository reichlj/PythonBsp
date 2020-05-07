import pandas as pd

cities = { 'name': ['London','Berlin','Madrid',
                    'Rome','Paris','Vienna'],
    'population' : [8615246,3562166,3165235,
                    2874038,2273305,1805681],
    'country'    : ['England','Germany','Spain',
                    'Italy','France','Austria'] }

city_frame = pd.DataFrame(cities)
city_frame.rename(columns=
    {'name':'Nume','country':'tara','population':'populatie'},
    inplace = True)
print(city_frame)
