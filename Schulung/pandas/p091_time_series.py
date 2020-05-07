import pandas as pd

index = pd.date_range('12/24/1970','01/03/1971')
print(index)
print('---------------------------------')
index = pd.date_range('12/24/1970',periods=4)
print(index)
print('---------------------------------')

index = pd.date_range('2017-04-07','2017-04-13',
                      freq='B')
print(index)
