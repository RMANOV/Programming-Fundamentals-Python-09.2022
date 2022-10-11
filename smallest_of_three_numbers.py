

def smallest_of_three_numbers(a, b, c):
    """Returns the smallest of three numbers"""
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_of_three_numbers(first_number, second_number, third_number))