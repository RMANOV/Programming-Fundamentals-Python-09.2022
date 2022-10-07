




number_list = input()

index_list = []
current_index = 0

input_string = input()
input_list = [input_string[i] for i in range(len(input_string))]

output_list = []

for digit in number_list:
    if digit == " ":
        current_index = 0
        continue
    else:     
        current_index += int(digit)
        index_list.append(current_index)
    
        



print(current_index)
