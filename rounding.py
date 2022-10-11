

def rounding(number):
    
    for number in initial_list:
        rounded_list.append(round(number))
    return rounded_list



initial_list = input().split()
initial_list = [float(i) for i in initial_list]
rounded_list = []
print(rounding(initial_list))