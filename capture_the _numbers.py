

import re

strings = input()

# Capture only the numbers in the string
while True:
    search_pattern = r'\d+' # r'(^|(?<=\s))(-)?(\d+)(\.\d+)?($|(?=\s))'    
    result = re.finditer(search_pattern, strings)
    strings = input()
    for match in result:
        print(match.group(0), end=' ')
    if strings == '':
        break
