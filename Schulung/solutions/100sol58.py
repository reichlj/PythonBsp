%matplotlib inline
import pandas as pd
data = pd.read_csv('data/smartphone_os.txt',
#                   header=1, # first data line lost
                   skiprows=1,
                   names=["Operating System","1Q16 Units","1Q16 Market Share (%)","1Q15 Units",
                          "1Q15 Market Share (%)",
                         ],
                   index_col="Operating System",
                  quotechar='"',
                   thousands=",",
                   delimiter=r"\s+",
                   engine = 'python',
                   skipfooter=2,
                  )
data.head()
data.dtypes
# plot bar
data[['1Q16 Units','1Q15 Units']].head()
data[['1Q15 Units','1Q16 Units']].plot(kind='bar')
