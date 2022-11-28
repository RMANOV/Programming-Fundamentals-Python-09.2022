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
car_dict = {
    input().split("|")[0]: input().split("|")[1:] for _ in range(number_of_cars)
}

command = input()

while not command == "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        car, distance, fuel = command[1:]
        distance = int(distance)
        fuel = int(fuel)
        if int(car_dict[car][1]) >= fuel:
            car_dict[car][0] = str(int(car_dict[car][0]) + distance)
            car_dict[car][1] = str(int(car_dict[car][1]) - fuel)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if int(car_dict[car][0]) >= 100000:
                print(f"Time to sell the {car}!")
                del car_dict[car]
        else:
            print("Not enough fuel to make that ride")
    elif command[0] == "Refuel":
        if int(car_dict[command[1]][1]) + int(command[2]) > 75:
            print(f"{command[1]} refueled with {75 - int(car_dict[command[1]][1])} liters")
            car_dict[command[1]][1] = str(75)
        else:
            car_dict[command[1]][1] = str(int(car_dict[command[1]][1]) + int(command[2]))
            print(f"{command[1]} refueled with {command[2]} liters")
    elif command[0] == "Revert":
        if int(car_dict[command[1]][0]) - int(command[2]) < 10000:
            car_dict[command[1]][0] = str(10000)
        else:
            car_dict[command[1]][0] = str(int(car_dict[command[1]][0]) - int(command[2]))
            print(f"{command[1]} mileage decreased by {command[2]} kilometers")
    command = input()

print(*[f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt." for car, [mileage, fuel] in car_dict.items()], sep="\n")

