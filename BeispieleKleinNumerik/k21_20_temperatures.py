import pandas as pd

df = pd.read_csv('temperatures.csv',sep=';',index_col=0,decimal=',')
print(df.head())
print(df.mean())
average_temp_series = df.mean(axis=1)
print(type(average_temp_series))
print(average_temp_series[:8])

sensors = df.columns.values
df = df.drop(sensors, axis =1)
print('df[:5]')
print(df[:5])
df = df.assign(temperature=average_temp_series)
print(df[:5])