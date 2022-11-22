

import re

numbers = input()

# A number has the following characteristics:
# •	Has either whitespace before it or the start of the string (match either ^ or what's called a positive lookbehind). The entire syntax for the beginning of your RegEx might look something like "(^|(?<=\s))".
# •	The number might or might not be negative, so it might have a hyphen on its left side ("-").
# •	It consists of one or more digits.
# •	Might or might not have digits after the decimal point
# •	The decimal part (if it exists) consists of a period (".") and one or more digits after it. Use a capturing group.
# •	Has either whitespace before it or the end of the string (match either $ or what's called a positive lookahead). The syntax for the end of the RegEx might look something like "($|(?=\s))".

search_pattern = r'(^|(?<=\s))(-)?(\d+)(\.\d+)?($|(?=\s))'
result = re.finditer(search_pattern, numbers)
for match in result:
    print(match.group(0), end=' ')