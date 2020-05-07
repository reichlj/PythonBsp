import pandas as pd

fruits = ['peaches','oranges','cherries','pears']
quantities = [20, 33, 52, 10]
quantities2 = [22, 37, 45, 22]
sales1 = pd.Series(quantities,index=fruits)
sales2 = pd.Series(quantities2,index=fruits)

df = pd.concat([sales1,sales2],axis=1)
print(df)

print('\nRenaming column names')
df.columns = ['sales1','sales2']
print(df)

df = pd.concat([sales1,sales2])
print(df)
