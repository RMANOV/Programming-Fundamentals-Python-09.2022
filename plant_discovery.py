

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
        # add plant to the dictionary
        plant_dictionary[plant] = {"rarity": 0, "rating": [rating]}

def update_plant(plant_dictionary, plant, new_rarity):
    if plant in plant_dictionary:
        plant_dictionary[plant]["rarity"] = new_rarity
    else:
        # add plant to the dictionary
        plant_dictionary[plant] = {"rarity": new_rarity, "rating": []}

def reset_plant(plant_dictionary, plant):
    if plant in plant_dictionary:
        plant_dictionary[plant]["rating"] = []
    else:
        return None
        

def average_rating(plant_dictionary):
    if len(plant_dictionary["rating"]) == 0:
        return 0
    return sum(plant_dictionary["rating"]) / len(plant_dictionary["rating"])

def print_plants(plant_dictionary):
    print("Plants for the exhibition:")
    print(*[f"- {plant}; Rarity: {plant_dictionary[plant]['rarity']}; Rating: {average_rating(plant_dictionary[plant]):.2f}" for plant in plant_dictionary], sep="\n")
    # print the plants sorted by rarity in descending order, then by rating in descending order - if the rarity is the same - 
    # withouth divise by zero error
    # print(*[f"- {plant}; Rarity: {plant_dictionary[plant]['rarity']}; Rating: {sum(plant_dictionary[plant]['rating']) / len(plant_dictionary[plant]['rating']):.2f}" for plant in sorted(plant_dictionary, key=lambda x: (-plant_dictionary[x]["rarity"], -sum(plant_dictionary[x]["rating"]) / len(plant_dictionary[x]["rating"]) if len(plant_dictionary[x]["rating"]) > 0 else 0))], sep="\n")
    # for plant, plant_info in sorted(plant_dictionary.items(), key=lambda x: (-x[1]["rarity"], -sum(x[1]["rating"]) / len(x[1]["rating"]) if len(x[1]["rating"]) > 0 else 0)):
    #     print(f"- {plant}; Rarity: {plant_dictionary[plant]['rarity']}; Rating: {sum(plant_dictionary[plant]['rating']) / len(plant_dictionary[plant]['rating']):.2f}")
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