

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

def filing_the_plant_dictionary(n):
    plant_dictionary = {}
    for _ in range(n):
        plant, rarity = input().split("<->")
        plant_dictionary[plant] = {"rarity": int(rarity), "rating": []}
    return plant_dictionary

def rating_plant(plant_dictionary, plant, rating):
    if plant in plant_dictionary:
        plant_dictionary[plant]["rating"].append(rating)
    else:
        print("error")

def update_plant(plant_dictionary, plant, new_rarity):
    if plant in plant_dictionary:
        plant_dictionary[plant]["rarity"] = new_rarity
    else:
        print("error")

def reset_plant(plant_dictionary, plant):
    if plant in plant_dictionary:
        plant_dictionary[plant]["rating"] = []
    else:
        print("error")

def print_plants(plant_dictionary):
    print("Plants for the exhibition:")
    if plant_dictionary:
        for plant, plant_info in sorted(plant_dictionary.items(), key=lambda x: (-x[1]["rarity"], -sum(x[1]["rating"]) / len(x[1]["rating"]))):
            print(f"- {plant}; Rarity: {plant_info['rarity']}; Rating: {sum(plant_info['rating']) / len(plant_info['rating']):.2f}")
    # if len(plant_dictionary) > 0:
    #     for plant, value in sorted(plant_dictionary.items(), key=lambda x: (-x[1]["rarity"], -sum(x[1]["rating"]) / len(x[1]["rating"]))):
    #         print(f"- {plant}; Rarity: {value['rarity']}; Rating: {sum(value['rating']) / len(value['rating']):.2f}")
    # else:
    #     print("error")

def plant_discovery():
    n = int(input())
    plant_dictionary = filing_the_plant_dictionary(n)
    while True:
        command = input()
        if command == "Exhibition":
            break
        command, plant = command.split(": ")
        value_list = plant.split(" - ")
        value = int(value_list[1]) if len(value_list) > 1 else value_list[0]
        if command == "Rate":
            rating_plant(plant_dictionary, plant, int(value))
        elif command == "Update":
            update_plant(plant_dictionary, plant, int(value))
        elif command == "Reset":
            reset_plant(plant_dictionary, plant)
    print_plants(plant_dictionary)

plant_discovery()