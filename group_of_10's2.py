initial_list_unsorted = [int(i) for i in input().split(", ")]

for n in range(1,11):
    list = [x for x in initial_list_unsorted if 10*(n-1) < x <= 10*n]
    if len(list) > 0:
        print(f"Group of {10*n}'s: {list}")