

initial_string = input()
string_list = list(initial_string)
explosive_power = 0

for i in range(len(string_list)):
    if string_list[i] == ">":
        explosive_power += int(string_list[i + 1])
    elif explosive_power > 0:
        string_list[i] = ""
        explosive_power -= 1

string_list = [x for x in string_list if x != ""]
print("".join(string_list))


# for char in initial_string:
#     if explosive_power > 0 and char != ">":
#         explosive_power -= 1
#         continue
#     elif char == ">":
#         explosive_power += int(initial_string[initial_string.index(char) + 1])
#     final_string += char
# print(final_string)

#     if char != ">" and explosive_power > 0:
#         explosive_power -= 1
#     elif char == ">":
#         explosive_power += int(initial_string[initial_string.index(char) + 1])
#         final_string += char
#     else:
#         final_string += char
# print(final_string)
     

#     if char == ">":
#         final_string += char
#         explosive_power += int(initial_string[initial_string.index(char) + 1])
#     elif explosive_power > 0:
#         explosive_power -= 1
#         continue
#     else:
#         final_string += char
        
# print(final_string)

# for char in range(len(initial_string)):
#     if initial_string[char] != '>' and explosive_power > 0:
#         explosive_power -= 1
#     elif initial_string[char] == '>':
#         final_string += initial_string[char]
#         explosive_power += int(initial_string[char + 1])
#     else:
#         final_string += initial_string[char]

# print(final_string)
