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
    
    


print(task_list)