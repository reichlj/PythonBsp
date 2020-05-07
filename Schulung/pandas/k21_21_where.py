import pandas as pd
import numpy as np

A = np.random.randint(1,30,(4,2))
print(A)
df = pd.DataFrame(A,columns=['Foo','Bar'])
m = df%2 == 0
print(m)
df.where(m,-df,inplace=True)
