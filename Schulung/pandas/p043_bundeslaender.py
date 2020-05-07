import pandas as pd
import numpy as np
laender = pd.read_csv("bundeslaender.txt",sep=" ")

laender.insert(loc=len(laender.columns),column = 'population',value=np.nan)
laender.insert(loc=len(laender.columns),column = 'density',value=np.nan)
laender['population'] = laender['male'] + laender['female']
laender['density'] = 1000*laender['population']/laender['area']

print(laender)

print(laender[ laender['area']>30000 ] )
print("******'area'>30000 & 'population'>10000")
print(laender.loc[ (laender['area']>30000) & 
                   (laender['population']>10000) ] )
print("******'density'>300")
print(laender[ laender['density']>300 ] )

laender = pd.read_csv("bundeslaender.txt",sep=" ")
laender.insert(loc=len(laender.columns),
               column = 'population',
               value=laender['male'] + laender['female'])
laender.insert(loc=len(laender.columns),
               column = 'density',
               value=1000*laender['population']/laender['area'])
print(laender)