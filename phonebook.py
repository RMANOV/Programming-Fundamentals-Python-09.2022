

phonebook = {}
command = input().split('-')

while not len(command) == 1:
    phonebook[command[0]] = command[1]
    command = input().split('-')

    if len(command) ==1:
        break
    
    command = input().split('-')

number_searched_names = int(command[0])
command = input()

for _ in range(number_searched_names):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
        
# Path: phonebook.py
        
