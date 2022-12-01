

# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
# •	If the data type is an int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is a string, surround the input with "$".
# Print the result on the console.

def multiply_by_2(num):
    return num * 2

def multiply_by_1_5(num):
    return f"{num * 1.5:.2f}"

def surround_with_dollar_sign(string):
    return f"${string}$"

def aquire_input():
    return input()

def main():
    data_type = input()
    if data_type == "int":
        print(multiply_by_2(int(aquire_input())))
    elif data_type == "real":
        print(multiply_by_1_5(float(aquire_input())))
    elif data_type == "string":
        print(surround_with_dollar_sign(aquire_input()))

main()















# def get_data_type():
#     if 
# # # How to get the data type?
# #     num = input()
# #     if num.isdigit():
# #         return "int"
# #     elif num.replace(".", "").isdigit():
# #         return "real"
# #     elif num.isalpha():
# #         return "string"
# #     else:
# #         return "unknown"

# def multiply_by_two(num):
#     return num * 2

# def multiply_by_one_and_half(num):
#     return num * 1.5

# def surround_with_dollar_sign(num):
#     return "$" + num + "$"

# def print_result(result):
#     print(result)

# def main():
#     data_type = get_data_type()
#     num = input()
#     if data_type == "int":
#         result = multiply_by_two(int(num))
#     elif data_type == "real":
#         result = multiply_by_one_and_half(float(num))
#     elif data_type == "string":
#         result = surround_with_dollar_sign(num)
#     print_result(result)

# main()
