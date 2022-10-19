from re import X


initial_list_unsorted = [int(i) for i in input().split(", ")]

for n in range(1,11):
    list = [x for x in initial_list_unsorted if 10*(n-1) < x <= 10*n]
    initial_list_unsorted = [x for x in initial_list_unsorted if x not in list]
    if n<11 and len(list)>=0:
        print(f"Group of {n*10}'s: {list}")
    if initial_list_unsorted == []:
        break


 

