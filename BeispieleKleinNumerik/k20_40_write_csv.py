import pandas as pd

excel_file = pd.ExcelFile('sales.xls')

sheet = pd.read_excel(excel_file)
print(sheet)

document = {}
for sheet_name in excel_file.sheet_names:
    document[sheet_name] = excel_file.parse(sheet_name)
    
for sheet_name in document:
    print('\n' + sheet_name + ':')    
    print(document[sheet_name])