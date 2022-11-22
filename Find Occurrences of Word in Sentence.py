

import re

strings = input()
target_word = input()
repeat_count = 0
# Write a program that finds how many times a word is used in a string.
# The output is a single number indicating the number of times the string contains the word. 
# Note that letter case does not matter – it is case-insensitive.


search_pattern = r'\b' + target_word + r'\b'
result = re.findall(search_pattern, strings, re.IGNORECASE)

for word in result:
    repeat_count += 1

print(repeat_count)
