

number_of_lines = int(input())

list_of_positive_numbers = []
list_of_negative_numbers = []

for i in range(number_of_lines):
    number = int(input())
    if number >= 0:
        list_of_positive_numbers.append(number)
    else:
        list_of_negative_numbers.append(number)


print(f"Count of positives: {len(list_of_positive_numbers)}")

print(f"Sum of negatives: {(list_of_negative_numbers).count()}")
