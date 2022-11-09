

phonebook = {}
command = []
command = input().split('-')
count_of_searched_names = 0
while len(command) != 1:
    command = [x for x in input().split('-') if not x.isdigit()]
    phonebook = {x: int(y) for x, y in zip(command[::2], command[1::2])}
    
    if len(command) == 1 and command[0].isdigit():
        count_of_searched_names = int(command[0])
        break

for _ in range(count_of_searched_names):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')


# command = input().split('-')
# phonebook[command[0]] = command[1]



# while len(command) == 1:
#     if len(command) == 1:
#         count_of_searched_names = int(command[0])
#         for i in range(count_of_searched_names):
#             name = input()
#             if name in phonebook:
#                 print(f'{name} -> {phonebook[name]}')
#             else:
#                 print('Contact {name} does not exist.')
            


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
        
