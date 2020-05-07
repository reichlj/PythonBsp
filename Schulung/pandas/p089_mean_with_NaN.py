import pandas as pd

temps_with_NaN = pd.read_csv('temperatures_with_NaN.csv',
                            index_col=0)

cleansed_df = temps_with_NaN.dropna(thresh=5,axis=0)

average_temp_series = cleansed_df.mean(axis=1)
sensors = cleansed_df.columns.values

df = cleansed_df.drop(sensors,axis=1)
df = df.assign(temperature = average_temp_series)
print(df[:5])