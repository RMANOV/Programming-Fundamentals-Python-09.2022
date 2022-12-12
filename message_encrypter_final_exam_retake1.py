# Input
# Example for a valid message: 
# "*Request*: [I]|[s]|[i]|"
# Output
# The possible outputs are:
# •	"{tag}: {number1} {number2} {number3}"
# •	"Valid message not found!"

import re

counts_of_inputs = int(input())
search_pattern = r"(\*|@)([A-Z][a-z]{2,})\1: \[([A-Za-z])\]\|\[([A-Za-z])\]\|\[([A-Za-z])\]\|$"

for _ in range(counts_of_inputs):
    message = input()
    for match in re.finditer(search_pattern, message):
        tag = match.group(2)
        first_letter = ord(match.group(3))
        second_letter = ord(match.group(4))
        third_letter = ord(match.group(5))
        print(f"{tag}: {first_letter} {second_letter} {third_letter}")
    else:
        print("Valid message not found!")




























    # if message.startswith("*") and message.endswith("*"):
    #     message = message[1:-1]
    #     if message.count("[") == message.count("]"):
    #         tag = ""
    #         numbers = []
    #         for i in message:
    #             if i == "[":
    #                 tag += i
    #             elif i == "]":
    #                 tag += i
    #             elif i.isdigit():
    #                 numbers.append(i)
    #         if len(tag) == 2:
    #             print(f"{tag}: {' '.join(numbers)}")
    #         else:
    #             print("Valid message not found!")
    #     else:
    #         print("Valid message not found!")
    # else:
    #     print("Valid message not found!")
