

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


for i in initial_list_sorted:
    if i<10:
        list10.append(i)
        print(f"Group of 10's: {i}")
    # elif i<20:
    #     print(f"Group of 20's: {i}")
    # elif i<30:
    #     print(f"Group of 30's: {i}")
    # elif i<40:
    #     print(f"Group of 40's: {i}")
    # elif i<50:
    #     print(f"Group of 50's: {i}")
    # elif i<60:
    #     print(f"Group of 60's: {i}")
    # elif i<70:
    #     print(f"Group of 70's: {i}")
    # elif i<80:
    #     print(f"Group of 80's: {i}")
    # elif i<90:
    #     print(f"Group of 90's: {i}")
    # elif i<100:
    #     print(f"Group of 100's: {i}")

        
