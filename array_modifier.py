

initial_list = [int(i) for i in input().split()]

while True:
    command = input().split()
    if command[0] == "end":
        break
    elif command[0] == "swap":
        initial_list[int(command[1])], initial_list[int(command[2])] = initial_list[int(command[2])], initial_list[int(command[1])]
    elif command[0] == "multiply":
        initial_list[int(command[1])] *= initial_list[int(command[2])]
    elif command[0] == "decrease":
        initial_list = [i - 1 for i in initial_list]

print((", ").join([str(i) for i in initial_list]))
