import pandas as pd

exchange_rates = pd.read_csv("dollar_euro.txt",sep='\t')
print(type(exchange_rates))
print(exchange_rates)

exchange_rates = pd.read_csv("dollar_euro.txt",sep='\t',header=0,
                             names=['year','min','max','days'])
print(exchange_rates)

