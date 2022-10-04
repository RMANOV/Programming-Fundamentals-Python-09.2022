

initial_string = input().split()
remove_count = int(input())
initial_list = []
initial_list.append(initial_string)
final_list = []
lowest_number = 0

for i in initial_string:
    
    current_number = int(i)
    if current_number < lowest_number:
        lowest_number = current_number
        final_list.append(lowest_number)
    else:
        final_list.append(current_number)

for i in range(remove_count):
    final_list.remove(min(final_list))

print(final_list)













# final_list = {max(initial_list[0][i]) for i in range(len(initial_list[0])) if i < remove_count}
# print(final_list)

# for i in range(len(initial_list)):
#     current_number = int(initial_list[i])
#     for j in range (remove_count+1):
#         final_list.append(initial_list[i][j])
#         lowest_number = min(final_list)
#         final_list[i].remove(lowest_number)
#         print(final_list[i], end=", ")
