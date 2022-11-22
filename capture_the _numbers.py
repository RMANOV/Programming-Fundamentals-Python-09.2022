

import re

strings = input()

# Capture only the numbers in the string
while True:
    search_pattern = r'\d+'
    result = re.findall(search_pattern, strings)
    if result:
        print(''.join(result), end=' ')
        strings = strings.replace(''.join(result), '', 1)
    else:
        break
