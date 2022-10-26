


initial_list = [("||").join() for i in range(3)]

distance_in_light_years = 0
fuel = 0
ammunition = 0

while True:
    command = input()
    command = command.split("||")
    distance_in_light_years += int(command[1])
    fuel += int(command[2])
    ammunition += int(command[3])

    if command == "Titan":
        print("You have reached Titan!, all passengers are safe.")
        break
    
    if command[0] == "Travel":
        if fuel < distance_in_light_years
            print("Mission failed.")
            break
        else:
            fuel -= distance_in_light_years
            distance_in_light_years = 0
            print(f'The spaceship traveled {distance_in_light_years} light years.')
            break
    elif command[0] == "Enemy":
        command = command.split("||")
        enemys_ammunition = int(command[1])
        if ammunition==0 or fuel==0 or fuel < enemys_ammunition*2:
            print("Mission failed.")
            break
        if ammunition < enemys_ammunition:
            # try to run away
            fuel -= enemys_ammunition*2
            print("An enemys whit {enemys_ammunition} is outmaneuvered")
        else:
            ammunition -= enemys_ammunition
            print("An enemys whit {enemys_ammunition} armour is defeated.")
            break



  



























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
