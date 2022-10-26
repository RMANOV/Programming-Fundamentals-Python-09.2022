initial_list = [i for i in input().split("‖")]

distance_in_light_years = initial_list[0]
fuel = initial_list[1]
ammunition = initial_list[2]

while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {distance_in_light_years}")
        break
    elif command == "Status":
        print(f"Distance left: {distance_in_light_years}")
        print(f"Fuel left: {fuel}")
        print(f"Ammunition left: {ammunition}")
        break
    else:
        command = command.split("‖")
        if command[0] == "Fuel":
            fuel += int(command[1])
            print(f"Fuel added: {command[1]}")
            break
        elif command[0] == "Ammo":
            ammunition += int(command[1])
            print(f"Ammunition added: {command[1]}")
            break
        elif command[0] == "Move":
            if command[1] == "Nuke":
                if ammunition >= 1:
                    distance_in_light_years += int(command[2])
                    ammunition -= 1
                else:
                    print("Not enough ammunition. Game Over!")
                    break
            elif command[1] == "Refuel":
                if fuel >= 1:
                    distance_in_light_years += int(command[2])
                    fuel -= 1
                else:
                    print("Not enough fuel. Game Over!")
                    break
            elif command[1] == "Normal":
                distance_in_light_years += int(command[2])
        else:
            print("Invalid command.")
            break

# Path: travel_to_titan2.py
































































# while True:
#     command = input()

#     if command == "Titan":
#         print("You have reached Titan!, all passengers are safe.")
#         break

#     command = command.split("‖")
#     distance_in_light_years += int(command[0])
#     fuel += int(command[1])
#     ammunition += int(command[2])

#     if command[0] == "Travel":
#         if fuel < distance_in_light_years:
#             print("Mission failed.")
#             break
#         else:
#             fuel -= distance_in_light_years
#             distance_in_light_years = 0
#             print(f'The spaceship traveled {distance_in_light_years} light years.')
#             break
#     elif command[0] == "Enemy":
#         command = command.split("‖")
#         enemys_ammunition = int(command[1])
#         if ammunition==0 or fuel==0 or fuel < enemys_ammunition*2:
#             print("Mission failed.")
#             break
#         if ammunition < enemys_ammunition:
#             # try to run away
#             fuel -= enemys_ammunition*2
#             print("An enemys whit {enemys_ammunition} is outmaneuvered")
#         else:
#             ammunition -= enemys_ammunition
#             print("An enemys whit {enemys_ammunition} armour is defeated.")
#             break
#     elif command[0] == "Repair":
#         command = command.split("‖")
#         fuel += int(command[1])
#         ammunition += int(command[2])
#         print("Fuel added: {command[1]}")
#         print("Ammunition added: {command[2]}")
#         break
#     # elif command[0] == "Refuel":
#     #     command = command.split("‖")
#     #     fuel += int(command[1])
#     #     print("Fuel added: {command[1]}")
#     #     break
#     # elif command[0] == "Ammo":
#     #     command = command.split("||")
#     #     ammunition += int(command[1])
#     #     print("Ammunition added: {command[1]}")
#     #     break
#     # elif command[0] == "Status":
#     #     print(f"Distance left: {fuel}")
#     #     print(f"Fuel left: {fuel}")
#     #     print(f"Ammunition left: {ammunition}")
#     #     break
#     else:
#         print("Invalid command.")
#         break





  



























    #     if command[1] == "Fuel":
    #         fuel += int(command[2])
    #     elif command[1] == "Ammunition":
    #         ammunition += int(command[2])
    # elif command[0] == "Move":
    #     if command[1] == "Nuke":
    #         if ammunition >= 1:
    #             distance_in_light_years += int(command[2])
    #             ammunition -= 1
    #         else:
    #             print("Not enough ammunition to perform this trip!")
    #     elif command[1] == "Faster":
    #         if fuel >= int(command[2]):
    #             distance_in_light_years += int(command[2])
    #             fuel -= int(command[2])
    #         else:
    #             print("Not enough fuel to perform this trip!")
    # elif command[0] == "Travel":
    #     if command[1] == "Normal":
    #         if fuel >= int(command[2]):
    #             distance_in_light_years += int(command[2])
    #             fuel -= int(command[2])
    #         else:
    #             print("Not enough fuel to perform this trip!")
    #     elif command[1] == "Time":
    #         if fuel >= int(command[2]) * 1.5:
    #             distance_in_light_years += int(command[2])
    #             fuel -= int(command[2]) * 1.5
    #         else:
    #             print("Not enough fuel to perform this trip!")
    # elif command[0] == "Refuel":
    #     fuel += int(command[1])
    # elif command[0] == "Status":
    #     print(f"Total Distance: {distance_in_light_years}")
    #     print(f"Total Fuel: {fuel}")
    #     print(f"Total Ammunition: {ammunition}")
