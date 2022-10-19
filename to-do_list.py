task_list = []

while True :
    command = input()
    if command == "End":
        break
    task_list = command.split("-")