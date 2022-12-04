# Input
# •	The possible inputs are:
# o	Examples of valid eggs: "@red@*/54/", "#green##//2//", "@@@yellow#@*/%^&/36/", "@#blue@*/1//"
# o	Examples of invalid eggs: "##@InvalidColor##/54/", "@notc0l0r@*23*", "@invalid_color@/notnumber/"
# Output
# •	The possible outputs are:
# o	"You found {amount} {color} eggs!"


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


# patern_colors = r"([a-z]{3,})+"
# patern_amounts = r"(\d{1,})"
# patern_colors = r"([a-z]{3,})+"
# patern_amounts = r"(\d{1,})"

import re

initial_string = input()

patern_colors = r"([a-z]{3,})+"
patern_amounts = r"(\d{1,})"
colors_and_amounts = {}

for match in re.finditer(patern_colors, initial_string):
    color = match.group()
    if color not in colors_and_amounts:
        colors_and_amounts[color] = 0
for match in re.finditer(patern_amounts, initial_string):
    amount = match.group()
    colors_and_amounts[color] += int(amount)
#remove invalid colors and amounts
for color in colors_and_amounts:
    if colors_and_amounts[color] != 'red' or colors_and_amounts[color] != 'green' or colors_and_amounts[color] != 'blue' or colors_and_amounts[color] != 'yellow' or colors_and_amounts[color] != 'purple':
        del colors_and_amounts[color]

# print(colors_and_amounts)
for color in colors_and_amounts:
    print(f"You found {colors_and_amounts[color]} {color} eggs!")















# if re.findall(patern_colors, initial_string) and re.findall(patern_amounts, initial_string):
#     colors = re.findall(patern_colors, initial_string)
#     amounts = re.findall(patern_amounts, initial_string)
#     for color in colors:
#         for amount in amounts:
#             print(f"You found {amount} {color} eggs!")

# eggs = re.findall(patern_colors + patern_amounts, initial_string)


# # get the input
# def get_input():
#     initial_string = input()
#     return initial_string


# # create only the valid colors in dictionary
# def create_colors_dict(initial_string):
#     colors_and_amounts = {}
#     colors = ["red", "blue", "green", "yellow", "purple", "orange"]
#     for color in colors:
#         if color in initial_string:
#             colors_and_amounts[color] = 0
#     return colors_and_amounts


# # search only for the colors in the string and add the amounts to the dictionary
# def get_colors_and_amounts(initial_string, colors_and_amounts):
#     for color in colors_and_amounts:
#         pattern = (
#             r"(@|#){1,}"
#             + color
#             + r"(@|#){1,}"
#             + r"(\d{1,})"
#             + r"(\D{1,})"
#             + r"(\d{1,})"
#         )
#         matches = re.findall(pattern, initial_string)
#         for match in matches:
#             colors_and_amounts[color] += int(match[4])
#     return colors_and_amounts


# # print the results
# def print_results(colors_and_amounts):
#     for color in colors_and_amounts:
#         if colors_and_amounts[color] > 0:
#             print(f"You found {colors_and_amounts[color]} {color} eggs!")


# def main():
#     initial_string = get_input()
#     colors_and_amounts = create_colors_dict(initial_string)
#     colors_and_amounts = get_colors_and_amounts(initial_string, colors_and_amounts)
#     print_results(colors_and_amounts)


# main()

# def main():
#     initial_string = input()
#     find_colors_and_amounts(initial_string)


# def find_colors_and_amounts(initial_string):
#     colors_and_amounts = {}
#     # create only the valid colors in dictionary
#     colors = ["red", "blue", "green", "yellow", "purple", "orange"]

#     for color in colors:
#         if color in initial_string:
#             colors_and_amounts[color] = 0

#     # add the amounts to the dictionary
#     for color in colors_and_amounts:
#         pattern = r"(@|#)+" + color + r"(@|#)+\/(\d{1,})\/"
#         matches = re.finditer(pattern, initial_string)
#         for match in matches:
#             colors_and_amounts[color] += int(match.group(4))

#     # print the results
#     for color in colors_and_amounts.items():
#         if colors_and_amounts[color] > 0:
#             print(f"You found {colors_and_amounts[color]} {color} eggs!")


# main()


# colors_and_amounts = {}

# # create only the valid colors in dictionary
# colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# for color in colors:
#     if color in initial_string:
#         colors_and_amounts[color] = 0

# # add the amounts to the dictionary
# for color in colors_and_amounts:
#     pattern = r"(@|#)+" + color + r"(@|#)+\/(\d{1,})\/"
#     matches = re.finditer(pattern, initial_string)
#     for match in matches:
#         colors_and_amounts[color] += int(match.group(4))

# # print the results
# for color in colors_and_amounts.items():
#     if colors_and_amounts[color] > 0:
#         print(f"You found {colors_and_amounts[color]} {color} eggs!")

# for match in re.finditer(patern_colors, initial_string):
#     color = match.group()
#     if color != "red" and color != "green" and color != "yellow" and color != "purple":
#         continue
#     colors_and_amounts[color] = 0

#     for match in re.finditer(patern_amounts, initial_string):
#         amount = match.group()
#         colors_and_amounts[color] = amount
#         print(f"You found {amount} {color} eggs!")
#         break


# colors_and_amounts = {}

# for match in re.finditer(patern_colors, initial_string):
#     color = match.group()
#     if color != "red" and color != "green" and color != "yellow" and color != "purple":
#         continue
#     colors_and_amounts[color] = 0


#     for match in re.finditer(patern_amounts, initial_string):
#         amount = match.group()
#         colors_and_amounts[color] += amount

# for color, amount in colors_and_amounts.items():
#     print(f"You found {amount} {color} eggs!")


# for match in re.finditer(patern_colors, initial_string):
#     color = match.group()
#     if color != "red" and color != "green" and color != "yellow" and color != "purple":
#         continue
#     colors_and_amounts[color] = 0


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
