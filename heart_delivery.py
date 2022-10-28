

initial_list_of_houses = [int(i) for i in input().split("@")]

while True:
    command = input()
    if command == "Love!":
        break
    command = command.split()
    jump_length = int(command[1])
    current_house = 0
    for i in range(jump_length):
        current_house += 1
        if current_house > len(initial_list_of_houses) - 1:
            current_house = 0
    if initial_list_of_houses[current_house] == 0:
        print(f"Place {current_house} already had Valentine's day.")
    else:
        initial_list_of_houses[current_house] -= 2
        if initial_list_of_houses[current_house] == 0:
            print(f"Place {current_house} has Valentine's day.")