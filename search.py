

number_of_lines = int(input())
passwordt = input()
initial_list = []

for i in range(number_of_lines):
    initial_string = input()
    initial_list.append(initial_string)

print(initial_list)

for j in range(len(initial_list)-1,-1,-1):
    elementt = initial_list[j]

    if passwordt not in elementt:
        initial_list.remove(elementt)
print(initial_list)
