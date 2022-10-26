import pandas as pd

# open specific excel file from a folder
df = pd.read_excel(r'C:\Users\r.manov\Desktop\Test_Pandas.xlsx', sheet_name='Sheet1')

# make cell "A17" active
df.loc[16, 1] = 'Active'

# In active cell "A17" write "Active"
df.loc[16, 1] = 'Active'

# move to cell "A18" and write "Active"
df.loc[17, 1] = 'Active'

# move to cell "A19" and write 19
df.loc[18, 1] = 19

# move to cell "A20" and write 20
df.loc[19, 1] = 20

# move to cell "A21" and write 21
df.loc[20, 1] = 21

# make color of active cell yellow
df.style.applymap(lambda x: 'background-color: yellow' if x == 'Active' else '')

# save the result in the same excel file
df.to_excel(r'C:\Users\r.manov\Desktop\Test_Pandas.xlsx', sheet_name='Sheet1', index=False)
