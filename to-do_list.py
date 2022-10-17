task_list = []

while True :
    command = input()
    if command == "End":
        break
    task_list.append(command)
    task_list.sort()
    task_list = [f"{index + 1}.{task}" for index, task in enumerate(task_list)]
    


print(task_list)