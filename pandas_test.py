import pandas as pd

# open Test_Pandas.xlsx file on the desktop
pd.read_excel('C:\\Users\\username\\r.manov\Desktop\\Test_Pandas.xlsx')


# Create a new sheet in the workbook Test_Pandas.xlsx and name it Sheet3
pd.DataFrame().to_excel('Test_Pandas.xlsx', sheet_name='Sheet3')

# Create a new sheet in the workbook Test_Pandas.xlsx and name it Sheet4
pd.DataFrame().to_excel('Test_Pandas.xlsx', sheet_name='Sheet4')

# go to cell A3 in the workbook Test_Pandas.xlsx and write the text "Hello World"
pd.DataFrame(['Hello World']).to_excel('Test_Pandas.xlsx', sheet_name='Sheet3', startrow=2, header=False, index=False)