import pandas as pd

df = pd.DataFrame([ [3.2,22], [10.8,28], [2.8,20.3] ],
                  index=['cat','dog','cat'],
                  columns=['weight','height'])
print(df)
s = df.stack()
print('--------------')
print(s)
print(type(s))                   
