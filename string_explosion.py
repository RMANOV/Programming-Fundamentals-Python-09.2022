

initial_string = input()
final_string = ""
explosive_power = 0

for i in range(len(initial_string)):
    if i == '>':
        final_string += '>'
        explosive_power += int(initial_string[i + 1])
    elif explosive_power > 0:
        explosive_power -= 1
    else:
        final_string += initial_string[i]

print(final_string)

