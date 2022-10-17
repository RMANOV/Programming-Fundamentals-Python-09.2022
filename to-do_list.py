

while True :
    command = input()
    if command == "End":
        break
    command = command.split("-")
    priority = int(command[0])
    task = command[1]
    
