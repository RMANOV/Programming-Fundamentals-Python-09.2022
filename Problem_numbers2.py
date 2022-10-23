

initial_list = [int(i) for i in input().split()]

while True:
    command = input().split()
    if command[0] == "Finish":
        break
    elif command[0] == "Add":
        initial_list.append(int(command[1]))
    elif command[0] == "Remove":
        if int(command[1]) in initial_list:
            initial_list.remove(int(command[1]))        
    elif command[0] == "Replace":
        if int(command[1]) in initial_list:
            initial_list[initial_list.index(int(command[1]))] = int(command[2])
    elif command[0] == "Collapse":
        for i in initial_list:
            if i < int(command[1]):
                initial_list.remove(i)

print(*initial_list)
  
