

phonebook = {}
command = input().split('-')

while not command.isdigit():
    command = input().split('-')
    phonebook[command[0]] = command[1]
    
for _ in range(int(command[0])):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
        
# Path: phonebook.py
        
