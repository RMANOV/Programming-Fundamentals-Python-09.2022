

train = int(input())
wagon = [0] * train
command = input()
while not command == "End":
    command = command.split()
    if command[0] == "add":
        wagon[-1] += int(command[1])
    elif command[0] == "insert":
        wagon[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        wagon[int(command[1])] -= int(command[2])
    command = input()
print(wagon)
