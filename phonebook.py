

phonebook = {}
command = []

command = input().split('-')
phonebook[command[0]] = command[1]

def add_contact():
    command = input().split('-')
    phonebook[command[0]] = command[1]
    return phonebook

def search_contact():
    command = input()
    if command in phonebook:
        print(f'{command} -> {phonebook[command]}')
    else:
        print(f'Contact {command} does not exist.')
        


# phonebook[command[0]] = command[1]
# while not len(command) == 1:
    
#     command = input().split('-')
#     phonebook[command[0]] = command[1]
#     if len(command) ==1:
#         break
    
#     command = input().split('-')

# number_searched_names = int(command[0])
# command = input()

# for _ in range(number_searched_names):
#     name = input()
#     if name in phonebook:
#         print(f'{name} -> {phonebook[name]}')
#     else:
#         print(f'Contact {name} does not exist.')
        
# Path: phonebook.py
        
