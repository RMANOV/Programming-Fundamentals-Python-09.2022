

# Snow White loves her dwarfs, but there are so many, and she doesn't know how to order them. 
# Does she order them by name? Or by the color of their hat? Or by physics? 
# She can't decide, so it's up to you to write a program that does it for her.
# You will be receiving several input lines which contain data about each dwarf in the following format:
# {dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
# The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
# You must store the data about the dwarfs in your program. There are several rules though:
# •	If 2 dwarfs have the same name but different colors, they should be considered different dwarfs, 
# and you should store them both.
# •	If 2 dwarfs have the same name and the same color, store the one with the higher physics.
# When you receive the command "Once upon a time", the input ends. 
# You must order the dwarfs by physics in descending order and then by the total count of dwarfs with the same hat color in descending order. 
# Then you must print them all.
# Input
# •	The input will consist of several input lines, containing dwarf data in the format, specified above.
# •	The input ends when you receive the command "Once upon a time". 
# Output
# •	As output, you must print the dwarfs, ordered in the way, specified above.
# •	The output format is: "({hat_color}) {name} <-> {physics}"
# Constraints
# •	The "dwarf_name" will be a string that may contain any ASCII character except ' ' (space), '<', ':', '>'.
# •	The "dwarf_hat_color" will be a string that may contain any ASCII character except ' ' (space), '<', ':', '>'.
# •	The "dwarf_physics" will be an integer in the range [0, 231 – 1].
# •	There will be no invalid input lines.
# •	If all sorting criteria fail, the order should be by order of input.

dwarfs = {}
# Get input and store dwarfs
command = input()
while command != "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    if dwarf_name not in dwarfs:
        dwarfs[dwarf_name] = {"color": dwarf_hat_color, "physics": dwarf_physics}
    else:
        if dwarfs[dwarf_name]["color"] != dwarf_hat_color and dwarfs[dwarf_name]["physics"] < dwarf_physics:
            update_dwarf = {dwarf_name: {"color": dwarf_hat_color, "physics": dwarf_physics}}
        else:
            if dwarfs[dwarf_name]["physics"] < dwarf_physics and dwarfs[dwarf_name]["color"] == dwarf_hat_color:
                update_dwarf = {dwarf_name: {"color": dwarf_hat_color, "physics": dwarf_physics}}
    command = input()
# Sort dwarfs
sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1]["physics"], -len([d for d in dwarfs.values() if d["color"] == x[1]["color"]])))

# Print dwarfs sorted by color and then by physics
# print(*[f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}" for dwarf in sorted_dwarfs], sep="\n")
# for dwarf in sorted_dwarfs:
#     print(f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}")
# sorted_by_color = sorted(sorted_dwarfs, key=lambda x: x[1]["color"])
# print(*[f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}" for dwarf in sorted_by_color], sep="\n")
sorted_by_color_and_physics = sorted(sorted_dwarfs, key=lambda x: (-x[1]["physics"], x[1]["color"]))
print(*[f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}" for dwarf in sorted_by_color_and_physics], sep="\n")