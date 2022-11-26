

# Write a program that finds all variable names in each string. 
# A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits. 
# Extract only their names without the underscore. 
# Try to do this only with regular expressions.
# The output consists of all variable names extracted and printed on a single line, separated by a comma.

import re

def extract_variable_names_whitout_underscores(text):
    return re.findall(r'(?<=\b_)[a-zA-Z0-9]+', text)

# def delete_underscore(text):
#     return text[1:]


def print_variable_names(variable_names):
    print(','.join(variable_names))

if __name__ == '__main__':
    text = input()
    variable_names = extract_variable_names_whitout_underscores(text)
    print_variable_names(variable_names)