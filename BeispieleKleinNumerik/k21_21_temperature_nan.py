import pandas as pd
import numpy as np

temp_df = pd.read_csv('temperatures.csv',sep=';',index_col=0,decimal=',')

random_df = pd.DataFrame(np.random.random(size=(54,6)),
                         columns=temp_df.columns.values,
                         index=temp_df.index)
nan_df = pd.DataFrame(np.nan,
                      columns=temp_df.columns.values,
                      index=temp_df.index)
df_bool = random_df < 0.7
print(df_bool[:5])
disturbed_data = temp_df.where(df_bool,nan_df)
print(disturbed_data[:10])

disturbed_data.to_csv('temperatures_withNaN.csv')
df = disturbed_data.dropna()
print(df)
