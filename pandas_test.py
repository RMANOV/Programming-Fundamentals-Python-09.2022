import pandas as pd

# open specific excel file from a folder
df = pd.read_excel(r'C:\Users\r.manov\Desktop\Test_Pandas.xlsx', sheet_name='Sheet1')

# get the column names
col_names = df.columns

# get the column values
col_values = df.values

# get the column values of a specific column
col_values = df['col1'].values

# get the numbers of rows and create a list of numbers
row_nums = list(range(1, len(df) + 1))

# create a new column
df['col2'] = row_nums

# create a new column with a specific value
df['col3'] = 'test'

# create a row with a specific value from a list
df.loc[len(df)] = ['test', 'test', 'test']