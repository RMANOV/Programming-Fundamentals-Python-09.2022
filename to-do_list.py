task_list = []
command = input()

while command != "End":
    prioritys, task = command.split("-")
    task_list.append([int(prioritys), task])
    command = input()
    task_list.sort()

print([to_do[1] for to_do in sorted(task_list, key=lambda x: x[0])])
