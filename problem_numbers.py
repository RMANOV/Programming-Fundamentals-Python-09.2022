

initial_list = [int(i) for i in input().split()]

initial_list_average = sum(initial_list) / len(initial_list)

above_the_average = [i for i in initial_list if i > initial_list_average]

above_the_average.sort(reverse=True)

if len(above_the_average) == 0:
    print("No")
else:
    print(" ".join([str(i) for i in above_the_average[:5]]))
