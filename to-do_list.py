task_list = []

while True :
    command = input()
    if command == "End":
        break
    command = command.split("-")
    prioryty = int(command[1])
    task = command[0]
    task_list.append((prioryty, task))
    task_list = [task_list[i] for i in range(len(task_list)) if i % 2 == 0]

print(task_list)