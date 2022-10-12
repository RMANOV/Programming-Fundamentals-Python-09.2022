def get_sum_of_digits(number):
    current_sum = 0
    while number > 0:
        current_sum += number % 10
        number = number // 10  # integer division
    return current_sum


initial_number = int(input())
print(initial_number)
print(get_sum_of_digits(initial_number))
