

import re

purchase = input()
total_cost = 0

# Write a program that calculates the total cost of bought furniture. 
# You will be given information about each purchase on separate lines until you receive the command "Purchase". 
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". 
# The price could be a floating-point or integer number. You should store the names of the furniture and the total price. 
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point.

while not purchase == 'Purchase':
    search_pattern = r'>>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'
    result = re.finditer(search_pattern, purchase)
    for item in result:
        total_cost += float(item.group('price')) * int(item.group('quantity'))
        print(item.group('name'))
    purchase = input()

print(f'Total money spend: {total_cost:.2f}')

