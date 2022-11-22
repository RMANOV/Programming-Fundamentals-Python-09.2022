

import re

strings = input()

# Capture only the numbers in the string

search_pattern = r'\d+'
result = re.findall(search_pattern, strings)
print(' '.join(result))
