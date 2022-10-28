

initial_list_of_houses = [int(i) for i in input().split("@")]
current_house = 0
while True:
    
    command = input()
    if command == "Love!":
        break
    command = command.split()
    jump_length = int(command[1])
    
    for i in range(1):
        current_house += jump_length
        if current_house == len(initial_list_of_houses):
            current_house = 0
        if initial_list_of_houses[current_house] == 0:
            print(f"Place {current_house} already had Valentine's day.")    
        else:
            initial_list_of_houses[current_house] -= 2
            if initial_list_of_houses[current_house] == 0:
                print(f"Place {current_house} has Valentine's day.")

print(f"Cupid's last position was {current_house}.")
if sum(initial_list_of_houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([i for i in initial_list_of_houses if i > 0])} places.")

















    #     current_house += 1
    #     if current_house > len(initial_list_of_houses) - 1:
    #         current_house = 0
    # if initial_list_of_houses[current_house] == 0:
    #     print(f"Place {current_house} already had Valentine's day.")
    # else:
    #     initial_list_of_houses[current_house] -= 2
    #     if initial_list_of_houses[current_house] == 0:
    #         print(f"Place {current_house} has Valentine's day.")

# print(f"Cupid's last position was {current_house}.")
# if sum(initial_list_of_houses) == 0:
#     print("Mission was successful.")
# else:
#     print(f"Cupid has failed {sum(initial_list_of_houses) // 2} places.")
