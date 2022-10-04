

initial_string = input().split()
remove_count = int(input())
initial_list = []
initial_list.append(initial_string)



initial_list =[int(i) for i in initial_string]



for i in range(remove_count):
    initial_list.remove(min(initial_list))

print(initial_list)



# how to do list comprehension?















# final_list = {max(initial_list[0][i]) for i in range(len(initial_list[0])) if i < remove_count}
# print(final_list)

# for i in range(len(initial_list)):
#     current_number = int(initial_list[i])
#     for j in range (remove_count+1):
#         final_list.append(initial_list[i][j])
#         lowest_number = min(final_list)
#         final_list[i].remove(lowest_number)
#         print(final_list[i], end=", ")
