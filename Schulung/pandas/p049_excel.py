import pandas as pd

x1 = pd.ExcelFile('excel_example.xlsx')

print(x1.sheet_names)

df1 = x1.parse('weekdays',index_col=0)
print(df1)

df2 = x1.parse('months',index_col=0)
print(df2.head())

writer = pd.ExcelWriter('excel_out.xlsx')
df1.to_excel(writer,'Sheet1')
df2.to_excel(writer,'Sheet2')
writer.save()
writer.close()
