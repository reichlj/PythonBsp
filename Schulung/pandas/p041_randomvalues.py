import pandas as pd
import numpy as np

names = ['Frank','Eve','Stella','Guido','Lara']
index = ['January','February','March','April','May','June','July',
         'August','September','October','November','December'] 

df = pd.DataFrame(np.random.rand(12,5)*1000,index=index,columns=names)

print(df)
