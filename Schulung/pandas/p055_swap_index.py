import pandas as pd


shop1 ={'foo': {2011:23,2012:25},
        'bar': {2011:13,2012:29} }
shop2 ={'foo': {2011:223,2012:225},
        'bar': {2011:213,2012:229} }
shop1 = pd.DataFrame(shop1)
shop2 = pd.DataFrame(shop2)
both_shops = shop1 + shop2
print('*** Sales of shop1 ***')
print(shop1)
print('*** Sales of shop1 and shop2 ***')
print(both_shops)

shops = pd.concat([shop1,shop2],keys=['one','two'])
print('*** Concatenation of shop1 and shop2 ***')
print(shops)

shops = shops.swaplevel()
print('Swapped indices')
print(shops)
print('Sorted Swapped indices')
shops.sort_index(inplace= True)
print(shops)
