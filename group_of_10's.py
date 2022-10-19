

initial_list_unsorted = [int(i) for i in input().split(", ")]
initial_list_sorted = sorted(initial_list_unsorted)
list10 = [x for x in initial_list_sorted if x <= 10]
list20 = [x for x in initial_list_sorted if 10 < x <= 20]
list30 = [x for x in initial_list_sorted if 20 < x <= 30]
list40 = [x for x in initial_list_sorted if 30 < x <= 40]
list50 = [x for x in initial_list_sorted if 40 < x <= 50]
list60 = [x for x in initial_list_sorted if 50 < x <= 60]
list70 = [x for x in initial_list_sorted if 60 < x <= 70]
list80 = [x for x in initial_list_sorted if 70 < x <= 80]
list90 = [x for x in initial_list_sorted if 80 < x <= 90]
list100 = [x for x in initial_list_sorted if 90 < x <= 100]


print(f"Group of 10's: {list10}")
print(f"Group of 20's: {list20}")
print(f"Group of 30's: {list30}")
print(f"Group of 40's: {list40}")
print(f"Group of 50's: {list50}")

if len(list60) > 0:
    print(f"Group of 60's: {list60}")
if len(list70) > 0:
    print(f"Group of 70's: {list70}")
if len(list80) > 0:
    print(f"Group of 80's: {list80}")
if len(list90) > 0:
    print(f"Group of 90's: {list90}")
if len(list100) > 0:
    print(f"Group of 100's: {list100}")
