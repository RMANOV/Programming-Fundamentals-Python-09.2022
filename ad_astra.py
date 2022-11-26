

# You are an astronaut who just embarked on a mission across the solar system. 
# Since you will be in space for a long time, you have packed a lot of food with you. 
# Create a program, which helps you identify how much food you have left and gives you information about its expiration date.
# On the first line of the input, you will be given a text string. 
# You must extract the information about the food and calculate the total calories. 
# First, you must extract the food info. 
# It will always follow the same pattern rules:
# •	It will be surrounded by "|" or "#" (only one of the two) in the following pattern: 
# #{item name}#{expiration date}#{calories}#   or 
# |{item name}|{expiration date}|{calories}|
# •	The item name will contain only lowercase and uppercase letters and whitespace
# •	The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be exactly two digits long
# •	The calories will be an integer between 0-10000
# Calculate the total calories of all food items and then determine how many days you can last with the food you have. 
# Keep in mind that you need 2000kcal a day.
# Input / Constraints
# •	You will receive a single string
# Output
# •	First, print the number of days you will be able to last with the food you have:
# "You have food to last you for: {days} days!"
# •	The output for each food item should look like this:
# "Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"


import re


def food_info(text):
    food_info = re.findall(r'(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1', text)
    return food_info

def food_calories(food_info):
    total_calories = 0
    for item in food_info:
        total_calories += int(item[3])
    return total_calories

def days_left(total_calories):
    days_left = total_calories // 2000
    return days_left

def print_food_info(food_info):
    for item in food_info:
        print
        print(f'Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}')

def print_days_left(days_left):
    print(f'You have food to last you for: {days_left} days!')

if __name__ == '__main__':
    text = input()
    food_info = food_info(text)
    total_calories = food_calories(food_info)
    days_left = days_left(total_calories)
    print_days_left(days_left)
    print_food_info(food_info)
