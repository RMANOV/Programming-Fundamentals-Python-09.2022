

from inspect import FullArgSpec


initial_list = [("||").join() for i in range(3)]

distance_in_light_years = 0
fuel = 0
ammunition = 0

while True:
    command = input()
    if command == "Titan":
        print("You have reached Titan!, all passengers are safe.")
        break
    command = command.split("||")
    if command[0] == "Travel":
        distance_in_light_years += int(command[1])
        fuel += int(command[2])
        ammunition += int(command[3])
        if fuel < distance_in_light_years
            print("Mission failed.")
            break
            
        else:
            print(f'The spaceship traveled {distance_in_light_years} light years.')
            break
    elif command[0] == "Fuel":
  



























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
