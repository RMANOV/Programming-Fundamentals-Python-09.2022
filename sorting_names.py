

initial_list = [initial_list for initial_list in input().split(", ")]

sorted_to_length = sorted(initial_list, key=lambda x: len(x), reverse=True)
sorted_alphabetically = sorted(sorted_to_length, key=lambda x: x)

print(sorted_alphabetically)