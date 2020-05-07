import pandas as pd

d = {
     'products': ['product1','product1','product2','product3'],
     'colours': ['blue','green','blue','green'],
     'customer_price': [2345.89,2390.50,1820.00,3100.00],
     'non_customer_price': [2445.89,2495.50,1980.00,3400.00] }

df = pd.DataFrame(d)
print(df)
print('-----------------------------')
df_pivot = df.pivot(index='products',
                    columns='colours')
print(df_pivot)
