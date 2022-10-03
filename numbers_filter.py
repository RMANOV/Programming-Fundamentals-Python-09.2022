

numbers_of_lines = int(input())

initial_list = []

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

for i in range(numbers_of_lines):
    initial_string = int(input())
    initial_list.append(initial_string)

command = input()
filtered_list = []


for element in initial_list:
    filtered_pased = (command == COMMAND_EVEN and int(element) % 2 == 0) or \
                        (command == COMMAND_ODD and int(element) % 2 != 0) or \
                        (command == COMMAND_NEGATIVE and int(element) < 0) or \
                        (command == COMMAND_POSITIVE and int(element) >= 0)
    if filtered_pased:
        filtered_list.append(element)




print(filtered_list)
