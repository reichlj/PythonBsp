import pandas as pd

df = pd.read_csv('temperatures.csv',
                 sep=';',
                 decimal=',')
print(df.head())
print('---------mean per zeile----------')
average_temp_series = df.mean(axis=1)
print(type(average_temp_series))
print(average_temp_series[:5])
print('-----------------------------')

sensors = df.columns.values
df = df.drop(sensors, axis =1)
print('df[:5]')
print(df[:5])
df = df.assign(temperature=average_temp_series)
print(df[:5])