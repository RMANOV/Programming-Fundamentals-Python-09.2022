

initial_string = input()
initial_list = list(initial_string)
digits = []
letters = []
special_characters = []

for char in initial_list:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        special_characters.append(char)

print(''.join(digits))
print(''.join(letters))
print(''.join(special_characters))
