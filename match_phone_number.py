

import re

phones = input()

# Compose the Regular Expression
# A valid number has the following characteristics:
# •	It starts with "+359"
# •	Then, it is followed by the area code (always 2)
# •	After that, it’s followed by the number itself:
# o	The number consists of 7 digits (separated into two groups of 3 and 4 digits, respectively). 
# •	The different parts are separated by either a space or a hyphen ('-').

# search_pattern = r'\+359\S2\b\s\d{3}\s\d{4}\b|\+359-2-\d{3}-\d{4}\b'
search_pattern = r'\+359\s2\s\d{3}\s\d{4}\b|\+359-2-\d{3}-\d{4}\b'
# result = re.findall(search_pattern, phones)
# print(', '.join(result))
result = re.findall(search_pattern, phones)
print(', '.join(result))
