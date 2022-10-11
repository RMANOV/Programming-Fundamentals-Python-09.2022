





def characters_in_range(start, end):
    return [chr(i) for i in range(ord(start) + 1, ord(end))]

first_character = input()
second_character = input()
print(*characters_in_range(first_character, second_character))