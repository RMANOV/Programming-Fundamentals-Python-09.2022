
def minimum_value(values):
    return min(values)

def maximum_value(values):
    return max(values)

def sum_of_values(values):
    return sum(values)


initial_list = input().split()
initial_list = [int(i) for i in initial_list]

print(f"The minimum number is {minimum_value(initial_list)}")
print(f"The maximum number is {maximum_value(initial_list)}")
print(f"The sum number is: {sum_of_values(initial_list)}")
