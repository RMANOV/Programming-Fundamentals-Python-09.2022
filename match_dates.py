

import re

dates = input()

# Every valid date has the following characteristics:
# •	It always starts with two digits, followed by a separator
# •	After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
# •	After that, it has a separator and exactly 4 digits (for the year).
# •	The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward-slash ("/").
# •	The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT). Use a group backreference to check for this.


search_pattern = r'\b(?P<day>\d{2})(?P<separator>[-./])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b'
result = re.findall(search_pattern, dates)
for day, separator, month, year in result:
    print(f'Day: {day}, Month: {month}, Year: {year}')
