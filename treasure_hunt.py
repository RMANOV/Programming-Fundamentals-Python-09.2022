

initial_loot_of_the_treasure_chest = [x for x in input().split("|")]
command = input()
while not command == "Yohoho!":
    command = command.split()
    if command[0] == "Loot":
        for item in command[1:]:
            if item not in initial_loot_of_the_treasure_chest:
                initial_loot_of_the_treasure_chest.insert(0, item)
    elif command[0] == "Drop":
        index = int(command[1])
        if 0 <= index < len(initial_loot_of_the_treasure_chest):
            initial_loot_of_the_treasure_chest.append(initial_loot_of_the_treasure_chest.pop(index))
    elif command[0] == "Steal":
        count = int(command[1])
        if count >= len(initial_loot_of_the_treasure_chest):
            print(", ".join(initial_loot_of_the_treasure_chest))
            initial_loot_of_the_treasure_chest.clear()
        else:
            print(", ".join(initial_loot_of_the_treasure_chest[-count:]))
            initial_loot_of_the_treasure_chest = initial_loot_of_the_treasure_chest[:-count]
    command = input()
if initial_loot_of_the_treasure_chest:
    print(f"Average treasure gain: {sum([len(x) for x in initial_loot_of_the_treasure_chest]) / len(initial_loot_of_the_treasure_chest):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

# Path: treasure_hunt.py
