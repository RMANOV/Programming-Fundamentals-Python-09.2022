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
    task_list = [task for priority, task in task_list]

print(task_list)