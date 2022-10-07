

number_list = input()
number_list = [str(i) for i in number_list]
index_list = []
current_index = 0

input_string = input()
input_list = [input_string[i] for i in range(len(input_string))]

output_list = []

for digit in number_list:
    if not digit == " ":
        current_index += number_list[digit]
    else:
        index_list.append(current_index)
        current_index = 0









print(number_list)
