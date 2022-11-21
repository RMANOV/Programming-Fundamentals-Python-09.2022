

import re

names = input()
# match all valid names that starts with Capital letter and after the first letter, it only contains lowercase letters
search_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
result = re.findall(search_pattern, names)
print(' '.join(result))
