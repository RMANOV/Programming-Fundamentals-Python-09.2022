

number_of_persons =int(input())
name = ''
age = ''

for i in range(number_of_persons):
    person_data = input().split()
    for j in range(len(person_data)):
        if person_data[j].startswith('@') and person_data[j].endswith('|'):
            name = person_data[j].replace('@', '').replace('|', '')
        elif person_data[j].startswith('#') and person_data[j].endswith('*'):
            age = person_data[j].replace('#', '').replace('*', '')
    print(f'{name} is {age} years old.')
    name = ''
    age = ''
    person_data.clear()

# Path: extract_person_information.py