
numbers_of_lines = int(input())
sum_of_chars = 0

for i in range(numbers_of_lines):
    line = input()
    
    for char in line:
        sum_of_chars += ord(char)

print(f'The sum equals: {sum_of_chars}')
