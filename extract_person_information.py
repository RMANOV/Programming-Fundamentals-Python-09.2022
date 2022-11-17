

number_of_persons =int(input())
name = ''
age = ''

for i in range(number_of_persons):
    person_data = input().split()
    for j in range(len(person_data)):
        if person_data[j].startswith('@'):
            # get all characters after @ and delete all characters after the |
            name = person_data[j][1:].split('|')[0]            
            # name = person_data[j].replace('@', '').replace('|', '')
        elif person_data[j].startswith('#'):
            # get all characters after # and delete all characters after the *
            age = person_data[j][1:].split('*')[0]
            # age = person_data[j].replace('#', '').replace('*', '')
    print(f'{name} is {age} years old.')
    name = ''
    age = ''
    person_data.clear()

# Path: extract_person_information.py