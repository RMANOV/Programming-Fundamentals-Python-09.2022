

resources = {}
command = input()


while not command == "stop":
    current_resource = command
    
    if current_resource not in resources:
        resources[current_resource] = 0
    if current_resource in resources:
        command = int(input())
        resources[current_resource] += command
        
    command = input()
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
    
    
    
#     if command.isdigit():
#         quantity = int(command)
#         resources[current_resource] += quantity
#     else:
#         if current_resource not in resources:
#             resources[current_resource] = 0
#     command = input()
    
# for resource, quantity in resources.items():
#     print(f"{resource} -> {quantity}")
    
    
    
    # resource = command[0]
    # quantity = int(command[1])
    # if resource not in resources:
    #     resources[resource] = 0
    # resources[resource] += quantity
    # command = input()
    
# for key, value in resources.items():
#     print(f"{key} -> {value}")
# print(f'{"".join([f"{key} -> {value})\n" for key, value in resources.items()])}')