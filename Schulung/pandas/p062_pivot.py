import pandas as pd

d = {
     'A': ['rot','grün','blau','rot','grün','blau'],
     'B': ['ein','zwei','ein','zwei','ein','zwei'],
     'C': [345,325,898,989,23,143],
     'D': [1,2,3,4,5,6] }

df = pd.DataFrame(d)
print(df)
print('==================')
df2 = df.pivot(index='A',columns='B',values='C')
print(df2)
print('==================')
df3 = df.pivot(index='A',columns='B',values=['C','D'])
print(df3)