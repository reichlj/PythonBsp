import pandas as pd

cities = { 'name': ['London','Berlin','Madrid','Rome','Paris'],
           'population' : [8615246,3562166,3165235,2874038,2273305],
           'country' : ['England','Germany','Spain','Italy','France'] }
ordinals = ["first","second","third","fourth","fifth"]
city_frame = pd.DataFrame(cities,index=ordinals)
print(city_frame)

city_frame = pd.DataFrame(cities,columns = ['name','country','population'])
print(city_frame)

city_frame= city_frame.reindex(index=[0,2,4,1,3],columns = ['name','country','population'])
print(city_frame)

city_frame.rename(columns = {'name':'nume','country':'tara','population':'poulatie'}, inplace=True)
print(city_frame)
