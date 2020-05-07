import pandas as pd

multicols = pd.MultiIndex.from_tuples([('weight','kg'),('weight','pounds')])
df_multi_level_cols = pd.DataFrame(
                  [ [3.2,7.1], [10.8,23.8], [2.8,6.2] ],
                  index=['cat','dog','cat'],
                  columns=multicols)
print(df_multi_level_cols)
print('--------------')
print(df_multi_level_cols.stack())
