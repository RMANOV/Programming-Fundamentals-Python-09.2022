

number_list = input()
number_list = [str(i) for i in number_list]
index_list = []
current_index = 0

input_string = input()
input_list = [input_string[i] for i in range(len(input_string))]

output_list = []

for i in range(len(number_list)):
    if i != " ":
        current_index += int(i)
    index_list.append(current_index)
    current_index = 0    
        










print(current_index)
