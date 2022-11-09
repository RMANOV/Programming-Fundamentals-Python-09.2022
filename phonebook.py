

phonebook = {}
command = []

command = input().split('-')
phonebook[command[0]] = command[1]

while len(command) == 1:
    if len(command) == 1:
        count_of_searched_names = int(command[0])
        for i in range(count_of_searched_names):
            name = input()
            if name in phonebook:
                print(f'{name} -> {phonebook[name]}')
            else:
                print('Contact {name} does not exist.')
            


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
        
