def removing_vowels(list_of_words):
    vowels = ['a', 'o', 'u', 'e', 'i']

    list_of_words = [char for char in list_of_words if char not in vowels]
    return list_of_words



initial_list = input()
print("".join( removing_vowels(initial_list)))
