import pandas as pd

cities = { 'name': ['London','Berlin','Madrid',
                    'Rome','Paris','Vienna','Munich','Hamburg'],
    'population' : [8615246,3562166,3165235,
                    2874038,2273305,1805681,1493900,1760433],
    'country'    : ['England','Germany','Spain',
                    'Italy','France','Austria','Germany','Germany'] }

city_frame = pd.DataFrame(cities,
                          columns=['country','area','population'],
                          index=cities['name'])
city_frame['area'] = [1572.0, 891.85, 605.77, 1285.0,
                      105.4, 414.60, 310.40,755]
print(city_frame)
