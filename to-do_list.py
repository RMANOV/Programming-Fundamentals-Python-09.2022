task_list = []

while True :
    command = input()
    if command == "End":
        break
    command = command.split("-")
    priority = int(command[0])
    task = command[1]
    task_list.append((priority, task))
    task_list.sort()
    # remove the priority from the list with list comprehension
    task_list = [task for task in task_list if priority.isdigit() == True task_list.remove(priority)]

    print(task_list)