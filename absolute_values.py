

def absolute_values(numbers):
    """Return the absolute values of the numbers in the list."""
    numbers = [float(i) for i in numbers]
    return [abs(number) for number in numbers]



initial_list = input().split()
print(absolute_values(initial_list))
