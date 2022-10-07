

initial_list = input().split(", ")
initial_list = [int(i) for i in initial_list]

zeros = 0
for i in initial_list:
    if i == 0:
        zeros += 1
        initial_list.remove(i)
        initial_list.append(0)

print(initial_list)