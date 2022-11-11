

initial_string = input()
initial_list = list(initial_string)
digits = []
letters = []
special_characters = []

for i in initial_list:
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        letters.append(i)
    else:
        special_characters.append(i)

print(''.join(digits))
print(''.join(letters))
print(''.join(special_characters))
