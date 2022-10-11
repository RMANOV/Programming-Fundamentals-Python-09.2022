

def sorted_list(list):
    list.sort()
    return list



initial_list = input().split()
initial_list = [int(i) for i in initial_list]

print(sorted_list(initial_list))
