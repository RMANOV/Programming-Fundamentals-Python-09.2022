def sum_numbers(a, b):
    """Returns the sum of two numbers"""
    return a + b
def subtract_numbers(sum, c):
    """Returns the result of subtracting the third number from the sum of the first two"""
    return sum - c




first_number = int(input())
second_number = int(input())
third_number = int(input())


print(subtract_numbers(sum_numbers(first_number, second_number), third_number))