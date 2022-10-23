

initial_list_of_groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command = command.split()
    action = command[0]
    item = command[1]
    if action == "Urgent":
        if item not in initial_list_of_groceries:
            initial_list_of_groceries.insert(0, item)
    elif action == "Unnecessary":
        if item in initial_list_of_groceries:
            initial_list_of_groceries.remove(item)
    elif action == "Correct":
        old_item = item
        new_item = command[2]
        if old_item in initial_list_of_groceries:
            index = initial_list_of_groceries.index(old_item)
            initial_list_of_groceries[index] = new_item
    elif action == "Rearrange":
        if item in initial_list_of_groceries:
            initial_list_of_groceries.remove(item)
            initial_list_of_groceries.append(item)

print(", ".join(initial_list_of_groceries))

