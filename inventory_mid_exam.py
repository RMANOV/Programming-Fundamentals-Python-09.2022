

initial_list = [x for x in input().split(", ")]

while True:
    command = input()
    if command == "Craft!":
        break
    command = command.split(" - ")
    if command[0] == "Collect":
        if command[1] not in initial_list:
            initial_list.append(command[1])
    elif command[0] == "Drop":
        if command[1] in initial_list:
            initial_list.remove(command[1])
    elif command[0] == "Combine Items":
        command = command[1].split(":")
        if command[0] in initial_list:
            initial_list.insert(initial_list.index(command[0]) + 1, command[1])
    elif command[0] == "Renew":
        if command[1] in initial_list:
            initial_list.append(initial_list.pop(initial_list.index(command[1])))
print(", ".join(initial_list))

# Path: inventory_mid_exam.py
