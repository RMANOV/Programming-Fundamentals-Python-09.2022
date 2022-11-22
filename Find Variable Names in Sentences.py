import re

strings = input()

# Write a program that finds all variable names in each string. 
# A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits. 
# Extract only their names without the underscore.


search_pattern = r'(?<=_)[a-zA-Z0-9]+'
result = re.findall(search_pattern, strings)
print(','.join(result))
