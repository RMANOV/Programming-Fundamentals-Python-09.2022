

initial_string = input().split()
remove_count = int(input())
initial_list = []
initial_list.append(initial_string)
final_list = []
lowest_number = 0

for i in range(len(initial_list)):
    final_list.append(int(initial_list[i]))
    lowest_number = min(final_list)
    final_list.remove(lowest_number)
    remove_count-=1
    if remove_count == 0:
        print(final_list[i], end=", ")
        break
