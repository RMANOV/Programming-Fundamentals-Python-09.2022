

# current_input = input().split()
# symbols = ''.join(current_input)
# letters = {}
# for symbol in symbols:
#     if symbol not in letters.keys():
#         letters[symbol] = 0
#     letters[symbol] += 1
# for char, occurrences in letters.items():
#     print(f"{char} -> {occurrences}")

#create a dictionary to store the count of each character
initial_string = input()

dictionary = {}
for i in initial_string:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

# Check if the keys are alfanumeric and print the count of each character
dictionary = {k: v for k, v in dictionary.items() if k.isalnum()}
# print(f'{key} -> {value}' for key, value in dictionary.items())
for keys, values in dictionary.items():
    print(f'{keys} -> {values}')

# print(key + " -> " + str(value) for key, value in dictionary.items())
# for key, value in dictionary.items():
#         print(key + " -> " + str(value))
    # print(i + " -> " + str(dictionary[i]))
# print(i + " -> " + int(dictionary[i]) for i in dictionary)
