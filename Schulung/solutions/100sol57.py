%matplotlib inline
import pandas as pd
data = pd.read_csv('data/visitors_python_de.txt',
                   index_col=False,
                  quotechar='"',
                   thousands=",",
                   delimiter=r"\s+")
data.head()
data.columns
month_year =  data[["Month", "Year"]]
month_year.dtypes
month_year = month_year.apply(lambda x: x[0] + " " + str(x[1]), 
                              axis=1)
data["Month"] = month_year
del data["Year"]

data.set_index("Month", inplace=True)
def unit_convert(x):
    value, unit = x
    if unit == "MB":
        value *= 1024
    elif unit == "GB":
        value *= 1048576 # i.e. 1024 **2
    return value
b_and_u= data[["Bandwidth", "Unit"]]
bandwidth = b_and_u.apply(unit_convert, axis=1)
del data["Unit"]
data["Bandwidth"] = bandwidth
data.tail()
data[:-1][["Unique visitors", "Number of visits"]].plot()
