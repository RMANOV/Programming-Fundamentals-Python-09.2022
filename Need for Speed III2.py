# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain.
# On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
# "{car}|{mileage}|{fuel}"
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
# •	"Drive : {car} : {distance} : {fuel}":
# o	You need to drive the given distance, and you will need the given fuel to do that.
# If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
# o	If the car has the required fuel available in the tank, increase its mileage with the given distance,
# decrease its fuel with the given fuel,
# and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
# o	You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print: "Time to sell the {car}!"
# •	"Refuel : {car} : {fuel}":
# o	Refill the tank of your car.
# o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up.
# o	Print a message in the following format: "{car} refueled with {fuel} liters"
# •	"Revert : {car} : {kilometers}":
# o	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
# o	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
# DO NOT print anything.
# Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
# Input/Constraints
# •	The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
# •	The fuel and distance amounts in the commands will never be negative.
# •	The car names in the commands will always be valid cars in your possession.
# Output
# •	All the output messages with the appropriate formats are described in the problem description.

number_of_cars = int(input())
car_dict = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    car_dict[car] = {"mileage": mileage, "fuel": fuel}

command = input()

while not command == "Stop":
    command = command.split(" : ")
    action = command[0]
    car = command[1]

    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if car_dict[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car]["mileage"] += distance
            car_dict[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_dict[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del car_dict[car]

    elif action == "Refuel":
        fuel = int(command[2])
        if car_dict[car]["fuel"] + fuel > 75:
            fuel = 75 - car_dict[car]["fuel"]
        car_dict[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        kilometers = int(command[2])
        car_dict[car]["mileage"] -= kilometers
        if car_dict[car]["mileage"] < 10000:
            car_dict[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

# for car, value in sorted(car_dict.items(), key=lambda x: (-x[1]["mileage"], x[0])):
for car, value in car_dict.items():
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")


















# for _ in range(number_of_cars):
#     car, mileage, fuel = input().split("|")
#     car_dict[car] = {"mileage": int(mileage), "fuel": int(fuel)}

# command = input()

# while not command == "Stop":
#     command = command.split(" : ")
#     command, car, value = command[0], command[1], command[2:]
#     if command[0] == "Drive":
#         distance, fuel = int(value[0]), int(value[1])
#         if car_dict[car]["fuel"] < fuel:
#             print("Not enough fuel to make that ride")
#         else:
#             car_dict[car]["mileage"] += distance
#             car_dict[car]["fuel"] -= fuel
#             print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#             if car_dict[car]["mileage"] >= 100000:
#                 print(f"Time to sell the {car}!")
#                 del car_dict[car]
#     elif command[0] == "Refuel":
#         fuel = int(value[0])
#         if car_dict[car]["fuel"] + fuel > 75:
#             fuel = 75 - car_dict[car]["fuel"]
#         car_dict[car]["fuel"] += fuel
#         print(f"{car} refueled with {fuel} liters")
#     elif command[0] == "Revert":
#         kilometers = int(value[0])
#         car_dict[car]["mileage"] -= kilometers
#         if car_dict[car]["mileage"] < 10000:
#             car_dict[car]["mileage"] = 10000
#         else:
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#     command = input()

# for car, value in sorted(car_dict.items(), key=lambda x: (-x[1]["mileage"], x[0])):
#     print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")

























#         car, distance, fuel = command[1], int(command[2]), int(command[3])
#         # distance = int(distance)
#         # fuel = int(fuel)
#         if int(car_dict[car][1]) >= fuel:
#             car_dict[car][0] = str(int(car_dict[car][0]) + distance)
#             car_dict[car][1] = str(int(car_dict[car][1]) - fuel)
#             print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#             if int(car_dict[car][0]) >= 100000:
#                 print(f"Time to sell the {car}!")
#                 del car_dict[car]
#         else:
#             print("Not enough fuel to make that ride")
#     elif command[0] == "Refuel":
#         car_dict[command[1]][1] = str(min(75, int(car_dict[command[1]][1]) + int(command[2])))
#         if int(car_dict[command[1]][1]) == 75:
#             print(f"{command[1]} refueled with {command[2]} liters")
#         else:
#             print(f"{command[1]} refueled with {75 - int(car_dict[command[1]][1])} liters")
#         # if int(car_dict[command[2]][1]) + int(command[2]) > 75:
#         #     print(f"{command[1]} refueled with {75 - int(car_dict[command[1]][1])} liters")
#         #     car_dict[command[1]][1] = str(75)
#         # else:
#         #     car_dict[command[1]][1] = str(int(car_dict[command[1]][1]) + int(command[2]))
#         #     print(f"{command[1]} refueled with {command[2]} liters")
#     elif command[0] == "Revert":
#         # Change type of mileage to int
#         old_mileage = int(car_dict[command[2]][0])
#         # revert = int(command[2])
#         # old_mileage = car_dict[
#         # new_mileage = old_mileage - revert
#         # if new_mileage < 10000:
#         #     car_dict[command[2]][0] = str(10000)
#         # else:
#         #     car_dict[command[2]][0] = str(new_mileage)
#         #     print(f"{command[2]} mileage decreased by {revert} kilometers")

#         # if int(car_dict[command[1]][0]) - int(command[2]) < 10000:
#         #     car_dict[command[1]][0] = str(10000)
#         # else:
#         #     car_dict[command[1]][0] = str(int(car_dict[command[1]][0]) - int(command[2]))
#         #     print(f"{command[1]} mileage decreased by {command[2]} kilometers")
#     command = input()

# # print(*[f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt." for car, [mileage, fuel] in car_dict.items()], sep="\n")
# for car, [mileage, fuel] in car_dict.items():
#     print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
