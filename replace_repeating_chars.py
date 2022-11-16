

initial_string = input()
final_string = ''
if initial_string[0] == initial_string[1]:
    final_string += initial_string[0]
for i in range(len(initial_string)):
    if initial_string[i] != initial_string[i-1]:
        final_string += initial_string[i]

print(final_string)