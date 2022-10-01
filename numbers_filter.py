

numbers_of_lines = int(input())

initial_list = []

for i in range(numbers_of_lines):
    initial_string = input()
    initial_list.append(initial_string)

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

command = input()
filtered_list = []

for element in initial_list:

    filtered_passes = (
        (command == COMMAND_EVEN and element % 2 == 0) or \
        (command == COMMAND_ODD and element % 2 != 0) or \
        (command == COMMAND_NEGATIVE and element < 0) or \
        (command == COMMAND_POSITIVE and element >= 0)
    )

    if filtered_passes:
        filtered_list.append(element)


print(filtered_list)
