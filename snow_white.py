

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


def main():
    dwarfs = {}
    while True:
        line = input()
        if line == "Once upon a time":
            break
        dwarf_name, dwarf_hat_color, dwarf_physics = line.split(" <:> ")
        dwarf_physics = int(dwarf_physics)
        if dwarf_name not in dwarfs:
            dwarfs[dwarf_name] = {}
        if dwarf_hat_color not in dwarfs[dwarf_name]:
            dwarfs[dwarf_name][dwarf_hat_color] = dwarf_physics
        else:
            if dwarf_physics > dwarfs[dwarf_name][dwarf_hat_color]:
                dwarfs[dwarf_name][dwarf_hat_color] = dwarf_physics
    dwarfs = sorted(dwarfs.items(), key=lambda x: (-max(x[1].values()), -len(x[1])))
    # You must order the dwarfs by physics in descending order and then by the total count of dwarfs with the same hat color in descending order
    # # for dwarf_name, dwarf_hat_color in dwarfs:
    # #     for hat_color, physics in dwarf_hat_color.items():
    # #         print(f"({hat_color}) {dwarf_name} <-> {physics}")
    # sorted_dwarfs_physics_descending_and_by_count_of_same_hat_color_descending = sorted(dwarfs, key=lambda x: (-max(x[1].values()), -len(x[1])))
    # for dwarf_name, dwarf_hat_color in sorted_dwarfs_physics_descending_and_by_count_of_same_hat_color_descending:
    #     for hat_color, physics in dwarf_hat_color.items():
    #         print(f"({hat_color}) {dwarf_name} <-> {physics}")
    sorted_by_physics_descending = sorted(dwarfs, key=lambda x: -max(x[1].values()))
    # sorted_by_count_of_same_hat_color_descending = sorted(sorted_by_physics_descending, key=lambda x: -len(x[1]))
    sorted_by_count_of_same_hat_color_ascending = sorted(sorted_by_physics_descending, key=lambda x: len(x[1]))
    for dwarf_name, dwarf_hat_color in sorted_by_count_of_same_hat_color_ascending:
        for hat_color, physics in dwarf_hat_color.items():
            print(f"({hat_color}) {dwarf_name} <-> {physics}")

main()
















# dwarfs = {}
# command = input()

# while command != "Once upon a time":
#     name, color, physics = command.split(" <:> ")
#     physics = int(physics)
#     if name not in dwarfs:
#         dwarfs[name] = {}
#         dwarfs[name]["color"] = color
#         dwarfs[name]["physics"] = physics
#     else:
#         if dwarfs[name]["color"] == color:
#             if dwarfs[name]["physics"] < physics:
#                 dwarfs[name]["physics"] = physics
#         else:
#             dwarfs[name] = {}
#             dwarfs[name]["color"] = color
#             dwarfs[name]["physics"] = physics
#     command = input()
    
# dwarfs = dict(sorted(dwarfs.items(), key=lambda x: (-x[1]["physics"], -len([d for d in dwarfs.values() if d["color"] == x[1]["color"]]))))
# # print the dwarfs sorted by color, name and physics
# print(*[f"({dwarfs[dwarf]['color']}) {dwarf} <-> {dwarfs[dwarf]['physics']}" for dwarf in dwarfs], sep="\n")

# dwarfs = {}
# command = input()

# while command != "Once upon a time":
#     name, color, physics = command.split(" <:> ")
#     physics = int(physics)
#     if name not in dwarfs:
#         dwarfs[name] = {}
#         dwarfs[name]["color"] = color
#         dwarfs[name]["physics"] = physics
#     else:
#         if dwarfs[name]["color"] == color and dwarfs[name]["physics"] < physics:
#            dwarfs[name]["physics"] = physics
#         elif dwarfs[name]["color"] != color:
#             dwarfs[name]["color"] = color
#             dwarfs[name]["physics"] = physics
#         else:
#             # add new dwarf to the existing dictionary, with the same name but different color and different physics
#             dwarfs[name] = {}
#             dwarfs[name]["color"] = color
#             dwarfs[name]["physics"] = physics
#     command = input()

# # sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1]["physics"], -list(dwarfs.values()).count(x[1])))
# # print(*[f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}" for dwarf in sorted_dwarfs], sep="\n")

# # print(*[f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}" for dwarf in sorted(dwarfs.items(), key=lambda x: (-x[1]["physics"], -list(dwarfs.values()).count(x[1])))], sep="\n")
# sorted_by_color_and_name_and_physics = sorted(dwarfs.items(), key=lambda x: (-x[1]["physics"], -list(dwarfs.values()).count(x[1])))
# print(*[f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}" for dwarf in sorted_by_color_and_name_and_physics], sep="\n")











# dwarfs = {}
# # Get input and store dwarfs
# command = input()
# while command != "Once upon a time":
#     dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")
#     dwarf_physics = int(dwarf_physics)
#     if dwarf_name not in dwarfs and dwarf_hat_color not in dwarfs:
#         dwarfs[dwarf_name] = {"color": dwarf_hat_color, "physics": dwarf_physics}
#     else:
#         if dwarfs[dwarf_name]["color"] != dwarf_hat_color and dwarfs[dwarf_name]["physics"] != dwarf_physics:
#             dwarfs[dwarf_name] = {"color": dwarf_hat_color, "physics": dwarf_physics}
#         else:
#             if dwarfs[dwarf_name]["physics"] < dwarf_physics and dwarfs[dwarf_name]["color"] == dwarf_hat_color:
#                 dwarfs[dwarf_name] = {"color": dwarf_hat_color, "physics": dwarf_physics}
#     command = input()
# # Sort dwarfs
# sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1]["physics"], -len([d for d in dwarfs.values() if d["color"] == x[1]["color"]])))

# # Print dwarfs sorted by color and then by physics
# # print(*[f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}" for dwarf in sorted_dwarfs], sep="\n")
# # for dwarf in sorted_dwarfs:
# #     print(f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}")
# # sorted_by_color = sorted(sorted_dwarfs, key=lambda x: x[1]["color"])
# # print(*[f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}" for dwarf in sorted_by_color], sep="\n")
# sorted_by_color_and_physics = sorted(sorted_dwarfs, key=lambda x: (-x[1]["physics"], x[1]["color"]))
# print(*[f"({dwarf[1]['color']}) {dwarf[0]} <-> {dwarf[1]['physics']}" for dwarf in sorted_by_color_and_physics], sep="\n")