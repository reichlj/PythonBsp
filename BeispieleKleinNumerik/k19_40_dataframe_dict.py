import pandas as pd

cities = { 'name': ['London','Berlin','Madrid','Rome','Paris'],
           'population' : [8615246,3562166,3165235,2874038,2273305],
           'country' : ['England','Germany','Spain','Italy','France'] }
city_frame = pd.DataFrame(cities)
print(city_frame)
