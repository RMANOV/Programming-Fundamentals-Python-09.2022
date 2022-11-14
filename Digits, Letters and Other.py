

initial_string = input()
initial_list = list(initial_string)
digits = ''
letters = ''
special_characters = ''

for char in initial_list:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        special_characters += char

print((digits))
print((letters))
print((special_characters))
