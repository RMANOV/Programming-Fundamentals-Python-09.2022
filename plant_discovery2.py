# You have now returned from your world tour.
# On your way, you have discovered some new plants, and you want to gather some information about them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n.
# On the next n lines, you will be given some information about the plants that you have discovered in the format: "{plant}<->{rarity}".
# Store that information because you will need it later.
# If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# •	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# •	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# •	"Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.
# Input / Constraints
# •	You will receive the input as described above
# Output
# Plants for the exhibition:
# - Arnoldii; Rarity: 4; Rating: 0.00
# - Woodii; Rarity: 5; Rating: 7.50
# - Welwitschia; Rarity: 2; Rating: 7.00


plants = {}
number_of_plants = int(input())

first_plants = [input().split("<->") for _ in range(number_of_plants)]
plants = {plant: {"rarity": int(rarity), "rating": []} for plant, rarity in first_plants}

command = input()

while command != "Exhibition":
    command = command.split(": ")
    action = command[0]
    plant = command[1].split(" - ")[0]
    if plant not in plants:
        print("error")
    else:
        if action == "Rate":
            rating = int(command[1].split(" - ")[1])
            plants[plant]["rating"].append(rating)
        elif action == "Update":
            rarity = int(command[1].split(" - ")[1])
            plants[plant]["rarity"] = rarity
        elif action == "Reset":
            plants[plant]["rating"] = []
        else:
            print("error")
    command = input()

if command == "Exhibition":
    print("Plants for the exhibition:")
    for plant, values in plants.items():
        if len(values["rating"]) == 0:
            print(f"- {plant}; Rarity: {values['rarity']}; Rating: 0.00")
        else:
            print(f"- {plant}; Rarity: {values['rarity']}; Rating: {sum(values['rating']) / len(values['rating']):.2f}")

# if rating == [] or rating == [0]:
#     average_rating = 0
# else:
#     average_rating = {plant: sum(ratings) / len(ratings) for plant, ratings in plants.items() if ratings["rating"]}

# print("Plants for the exhibition:")
# print(*[f"- {plant}; Rarity: {rarity}; Rating: {average_rating[plant]:.2f}" for plant, rarity in plants.items()], sep="\n")
# print(*[f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {sum(plants[plant]['rating']) / len(plants[plant]['rating']):.2f}" for plant in plants], sep="\n")
