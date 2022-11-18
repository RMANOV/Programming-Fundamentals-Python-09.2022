

first_symbol = ord(input())
second_symbol = ord(input())
random_string = input()
ASCII_sum = 0

for i in range(len(random_string)):
    if first_symbol < ord(random_string[i]) < second_symbol:
        ASCII_sum += ord(random_string[i])

print(ASCII_sum)
