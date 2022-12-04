

# Input
# •	The possible inputs are:
# o	Examples of valid eggs: "@red@*/54/", "#green##//2//", "@@@yellow#@*/%^&/36/", "@#blue@*/1//"
# o	Examples of invalid eggs: "##@InvalidColor##/54/", "@notc0l0r@*23*", "@invalid_color@/notnumber/"
# Output
# •	The possible outputs are:
# o	"You found {amount} {color} eggs!"
# Examples
# •	You will receive a string.

# Input
# @@@@green@*/10/@yel0w@*26*#red#####//8//@limon*@*23*@@@red#*/%^&/6/@gree_een@/notnumber/###purple@@@@@*$%^&*/5/
# Output
# You found 10 green eggs!
# You found 8 red eggs!
# You found 6 red eggs!
# You found 5 purple eggs!




# match colors - they are only lowercase letters and minimum 3 letters
# match and amounts - only digits, minimum 1 digit, but maximum 2 digits
# between the colors and numbers - any non alfabetical symbols and non digits
# amounts -always after colors, suroounded by one or more / symbols
# colors - always before amounts, surrounded by one or more @ and # symbols
# #@##@red@#/8/@rEd@/2/#@purple@////10/@purple@/5/


import re


initial_string = input()

# patern_colors = r"([a-z]{3,})+"
# patern_amounts = r"(\d{1,})"


patern_colors = r"([a-z]{3,})+"
patern_amounts = r"(\d{1,})"
colors_and_amounts = {}

for match in re.finditer(patern_colors, initial_string):
    color = match.group()
    if color != "red" and color != "green" and color != "yellow" and color != "purple":
        continue
    colors_and_amounts[color] = 0
    
    
    
    
    
    
    
    
    
    
    
#     if color not in colors_and_amounts:
#         colors_and_amounts[color] = 0
#     for match in re.finditer(patern_amounts, initial_string):
#         amount = match.group()
#         colors_and_amounts[color] += int(amount)
        

# for color, amount in colors_and_amounts.items():
#     print(f"You found {amount} {color} eggs!")






# valid_eggs_and_colors = re.finditer(patern, initial_string)

# for egg in valid_eggs_and_colors:
#     color = egg.group("color")
#     numbers = egg.group("numbers")
#     numbers = [ord(x) for x in numbers]
#     numbers = [str(x) for x in numbers]
#     numbers = " ".join(numbers)
#     print(f"You found {len(numbers)} {color} eggs!")
#     print(f"Your numbers are: {numbers}")
