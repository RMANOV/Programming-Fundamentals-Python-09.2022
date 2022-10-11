





def even_numbers2(list1):
    final_list = [i for i in list1 if i % 2 == 0]
    final_list.sort()
    return final_list

    



initial_list = input().split()
initial_list = [int(x) for x in initial_list]
final_list = []
print(even_numbers2(initial_list))