# Input
# •	The possible commands are:
# o	"Add {particle} {index}"
# o	"Remove {index}"
# o	"Check Even"
# o	"Check Odd"
# o	"Done"
# Output
# •	The possible outputs are:
# o	"You crafted {weaponName}!"

mixed_part_of_weapon = input().split("|")

while True:
    command = input().split()
    if command[0] == "Done":
        break
    elif command[0] == "Check":
        if command[1] == "Even":
            for i in range(len(mixed_part_of_weapon)):
                if i % 2 == 0:
                    print(mixed_part_of_weapon[i], end=" ")
        elif command[1] == "Odd":
            for i in range(len(mixed_part_of_weapon)):
                if i % 2 != 0:
                    print(mixed_part_of_weapon[i], end=" ")
        print()
    elif command[0] == "Add":
        if 0 <= int(command[2]) < len(mixed_part_of_weapon):
            mixed_part_of_weapon.insert(int(command[2]), command[1])
    elif command[0] == "Remove":
        if 0 <= int(command[1]) < len(mixed_part_of_weapon):
            mixed_part_of_weapon.pop(int(command[1]))

print(f"You crafted {''.join(mixed_part_of_weapon)}!")