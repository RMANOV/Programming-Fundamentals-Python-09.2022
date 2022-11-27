

# You are a world traveler, and your next goal is to make a world tour. 
# To do that, you have to plan out everything first. 
# To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops. 
# Until you receive the command "Travel", you will be given some commands to manipulate that initial string.
# The commands can be:
# •	"Add Stop:{index}:{string}":
# o	Insert the given string at that index only if the index is valid
# •	"Remove Stop:{start_index}:{end_index}":
# o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	"Switch:{old_string}:{new_string}":
# o	If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string if it is valid!
# After the "Travel" command, print the following: "Ready for a world tour! Planned stops: {string}"
# Input / Constraints
# •	An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description


def main():
    stops = input()
    while True:
        command = input()
        if command == "Travel":
            break
        command = command.split(":")
        if command[0] == "Add Stop":
            index = int(command[1])
            string = command[2]
            if 0 <= index < len(stops):
                stops = stops[:index] + string + stops[index:]
            print(stops)
        elif command[0] == "Remove Stop":
            start_index = int(command[1])
            end_index = int(command[2])
            if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
                stops = stops[:start_index] + stops[end_index + 1:]
            print(stops)
        elif command[0] == "Switch":
            old_string = command[1]
            new_string = command[2]
            if old_string in stops:
                stops = stops.replace(old_string, new_string)
            print(stops)
    print(f"Ready for world tour! Planned stops: {stops}")
main()





# Get the initial string
# def get_initial_string():
#     initial_string = input()
#     return initial_string

# def get_command():
#     command = input()
#     return command

# def add_stop(initial_string, command):
#     command = command.split(":")
#     index = int(command[1])
#     string = command[2]
#     if index in range(len(initial_string)):
#         initial_string = initial_string[:index] + string + initial_string[index:]
#     return initial_string

# def remove_stop(initial_string, command):
#     command = command.split(":")
#     start_index = int(command[1])
#     end_index = int(command[2])
#     if start_index in range(len(initial_string)) and end_index in range(len(initial_string)):
#         initial_string = initial_string[:start_index] + initial_string[end_index + 1:]
#     return initial_string

# def switch(initial_string, command):
#     command = command.split(":")
#     old_string = command[1]
#     new_string = command[2]
#     if old_string in initial_string:
#         initial_string = initial_string.replace(old_string, new_string)
#     return initial_string

# def print_result(initial_string):
#     print(f"Ready for a world tour! Planned stops: {initial_string}")

# def main():
#     initial_string = get_initial_string()
#     command = get_command()
#     while not command == "Travel":
#         if "Add Stop" in command:
#             initial_string = add_stop(initial_string, command)
#             print(initial_string)
#         elif "Remove Stop" in command:
#             initial_string = remove_stop(initial_string, command)
#             print(initial_string)
#         elif "Switch" in command:
#             initial_string = switch(initial_string, command)
#             print(initial_string)
#         command = get_command()
#     print_result(initial_string)


# def initial_string():
#     initial_string = input()
#     return initial_string

# def add_stop(initial_string, index, string):
#     if index in range(len(initial_string)):
#         initial_string = initial_string[:index] + string + initial_string[index:]
#     return initial_string

# def remove_stop(initial_string, start_index, end_index):
#     if start_index in range(len(initial_string)) and end_index in range(len(initial_string)) and start_index < end_index:
#         initial_string = initial_string[:start_index] + initial_string[end_index + 1:]
#     return initial_string

# def switch(initial_string, old_string, new_string):
#     if old_string in initial_string:
#         initial_string = initial_string.replace(old_string, new_string)
#     return initial_string

# def print_string(initial_string):
#     print(f'Ready for a world tour! Planned stops: {initial_string}')

# def print_current_state(initial_string):
#     print(initial_string)

# def world_tour(initial_string):
#     command = input().split(':')
#     return command

# def main():
#     initial_string = initial_string()
#     command = world_tour(initial_string)
#     while command[0] != 'Travel':
#         if command[0] == 'Add Stop':
#             initial_string = add_stop(initial_string, int(command[1]), command[2])
#             print_current_state(initial_string)
#         elif command[0] == 'Remove Stop':
#             initial_string = remove_stop(initial_string, int(command[1]), int(command[2]))
#             print_current_state(initial_string)
#         elif command[0] == 'Switch':
#             initial_string = switch(initial_string, command[1], command[2])
#             print_current_state(initial_string)
#         command = world_tour(initial_string)
#     print_string(initial_string)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # commands = command[0]
    # second_string = command[1]
    
    # if commands == 'Add Stop':
    #     index = int(second_string)
    #     if index in range(len(initial_string)):
    #         string = command[2]
    #         initial_string = initial_string[:index] + string + initial_string[index:]
    #         print(initial_string)
    # elif commands == 'Remove Stop':
    #     start_index = int(second_string)
    #     end_index = int(command[2])
    #     if start_index in range(len(initial_string)) and end_index in range(len(initial_string)):
    #         initial_string = initial_string[:start_index] + initial_string[end_index + 1:]
    #         print(initial_string)
    # elif commands == 'Switch':
    #     old_string = second_string
    #     new_string = command[2]
    #     if old_string in initial_string:
    #         initial_string = initial_string.replace(old_string, new_string)
    #         print(initial_string)

    # command = input().split(':')
    
# print(f'Ready for a world tour! Planned stops: {initial_string}')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # command = command[0]
    # second_string = command[1]
    # if command == 'Add stop':
    #     index = command.split(':')[1]
    #     pass
    # if command == 'Remove stop':
    #     pass
    # if command == 'Switch stop':
    #     trird_string = command.split(':')[2]
    #     pass
    # command = command.split(':')
