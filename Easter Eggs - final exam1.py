

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

import re

initial_string = input()
patern = r"(@{1,}|#{1,})([A-Za-z]{3,})\1\*([A-Za-z]{1,})\3\*"
valid_eggs_and_colors = re.finditer(patern, initial_string)

for egg in valid_eggs_and_colors:
    color = egg.group("color")
    numbers = egg.group("numbers")
    numbers = [ord(x) for x in numbers]
    numbers = [str(x) for x in numbers]
    numbers = " ".join(numbers)
    print(f"You found {len(numbers)} {color} eggs!")
    print(f"Your numbers are: {numbers}")
