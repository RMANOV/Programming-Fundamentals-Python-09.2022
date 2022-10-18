task_list = []

while True :
    command = input()
    if command == "End":
        break
    task_list.append(command)
    task_list.sort()
    task_list = [command for digit in task_list if not digit.isdigit()]
    

print(task_list)