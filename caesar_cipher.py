

initial_string = input()
final_string = ""

# final_string = enumerate(chr(ord(initial_string[i]) + 3) for i in range(len(initial_string)))


for i in range(len(initial_string)):
    final_string += chr(ord(initial_string[i]) + 3)

print(final_string)
