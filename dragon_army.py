

# You need to categorize dragons by their type. 
# For each dragon, identified by name, keep information about his stats (damage, health, and armor). 
# Type is preserved as in the order of input, but dragons are sorted alphabetically by their name. 
# For each type, you should also print the average damage, health, and armor of the dragons. 
# For each dragon, print his own stats. 
# There may be missing stats in the input, though. 
# If a stat is missing you should assign its default values. Default values are as follows: 
# Health 250, damage 45, and armor 10. Missing stat will be marked as "null".
# The input is in the following format "{type} {name} {damage} {health} {armor}". 
# The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers. 
# Any of the integers may be assigned a "null" value. See the examples below for a better understanding of your task.
# If the same dragon is added a second time, the new stats should overwrite the previous ones. 
# Two dragons are considered equal if they match by both name and type.
# Input
# •	On the first line, you are given the number N -> the number of dragons to follow.
# •	On the next N lines, you are given input in the above-described format. There will be a single space separating each element.
# Output
# •	Print the aggregated data on the console.
# •	For each type, print the average stats of its dragons in the format "{type}::({damage}/{health}/{armor})".
# •	Damage, health, and armor should be rounded to two digits after the decimal separator.
# •	For each dragon, print its stats in the format "-{Name} -> damage: {damage}, health: {health}, armor: {armor}".
# Constraints
# •	N is in the range [1…100].
# •	The dragon type and name are one word only, starting with a capital letter.
# •	Damage health and armor are integers in the range [0 … 100000] or null.
# Input
# 5
# Red Bazgargal 100 2500 25
# Black Dargonax 200 3500 18
# Red Obsidion 220 2200 35
# Blue Kerizsa 60 2100 20
# Blue Algordox 65 1800 50

# Output
# Red::(160.00/2350.00/30.00)
# -Bazgargal -> damage: 100, health: 2500, armor: 25
# -Obsidion -> damage: 220, health: 2200, armor: 35
# Black::(200.00/3500.00/18.00)
# -Dargonax -> damage: 200, health: 3500, armor: 18
# Blue::(62.50/1950.00/35.00)
# -Algordox -> damage: 65, health: 1800, armor: 50
# -Kerizsa -> damage: 60, health: 2100, armor: 20
# Input2
# 4
# Gold Zzazx null 1000 10
# Gold Traxx 500 null 0
# Gold Xaarxx 250 1000 null
# Gold Ardrax 100 1055 50
# Output2
# Gold::(223.75/826.25/17.50)
# -Ardrax -> damage: 100, health: 1055, armor: 50
# -Traxx -> damage: 500, health: 250, armor: 0
# -Xaarxx -> damage: 250, health: 1000, armor: 10
# -Zzazx -> damage: 45, health: 1000, armor: 10








dragons = {}
number_of_dragons = int(input())


for _ in range(number_of_dragons):
    dragon_type, dragon_name, damage, health, armor = input().split()
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    if dragon_type not in dragons:
        dragons[dragon_type] = {}
    dragons[dragon_type][dragon_name] = [int(damage), int(health), int(armor)]

for dragon_type, dragon_name in dragons.items():
    average_damage = sum([damage for damage, _, _ in dragon_name.values()]) / len(dragon_name)
    average_health = sum([health for _, health, _ in dragon_name.values()]) / len(dragon_name)
    average_armor = sum([armor for _, _, armor in dragon_name.values()]) / len(dragon_name)
    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for dragon_name, stats in sorted(dragon_name.items()):
        print(f"-{dragon_name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")

# Calculate and print the stats for every dragon
