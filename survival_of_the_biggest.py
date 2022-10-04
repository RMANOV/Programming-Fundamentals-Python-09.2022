

initial_string = input().split()
remove_count = int(input())
initial_list = []
initial_list.append(initial_string)
final_list = []
lowest_number = 0

for i in range(len(initial_list)):
    current_number = int(initial_list[i])
    for j in range (remove_count+1):
        final_list.append(initial_list[i][j])
        lowest_number = min(final_list)
        final_list[i].remove(lowest_number)
        print(final_list[i], end=", ")
