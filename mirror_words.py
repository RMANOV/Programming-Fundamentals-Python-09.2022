

# On the first line of the input, you will be given a text string. 
# To win the competition, you have to find all hidden word pairs, read them, 
# and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. 
# Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols)
# •	Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), 
# they are a match, and you have to store them somewhere. 
# Examples of mirror words: 
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs, print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words, print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
# Input / Constraints
# •	You will recive a string.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description.
# •	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
# •	Each pair of mirror word must be printed with " <=> " between the words.

import re

target_string = input()

miror_words = [x for x in re.findall(r'(@|#)(?P<word_one>[a-zA-Z]{3,})\1\1(?P<word_two>[a-zA-Z]{3,})\1', target_string)]

for x in miror_words:
    if x[1] =='@' or x[1] == '#':
        miror_words.remove(x)

word_pairs = len(miror_words)

miror_words = [x for x in miror_words if x[1] == x[2][::-1]]

if word_pairs == 0:
    print('No word pairs found!')
else:
    print(f'{word_pairs} word pairs found!')

if len(miror_words) == 0:
    print('No mirror words!')
else:
    print(f'The mirror words are:')
    print(', '.join([f'{x[1]} <=> {x[2]}' for x in miror_words]))


# if not miror_words:
#     print('No word pairs found!')
#     print('No miror words!')
# else:
#     print(f'{len(miror_words)} word pairs found!')
#     print(f'The mirror words are:')
#     print(', '.join(mirror_word[1] + ' <=> ' + mirror_word[2] for mirror_word in miror_words))




# def is_mirror_word(word):
#     return word == word[::-1]

# def find_mirror_words(text):
#     pattern = r'(@|#)(?P<word_one>[A-Za-z]{3,})\1\1(?P<word_two>[A-Za-z]{3,})\1'
#     # pattern = r'([@#])(?P<word_one>[A-Za-z]{3,})\1\1(?P<word_two>[A-Za-z]{3,})\1'
#     matches = re.finditer(pattern, text)
#     mirror_words = []
#     for match in matches:
#         word_one = match.group('word_one')
#         word_two = match.group('word_two')
#         if is_mirror_word(word_two):
#             mirror_words.append(f'{word_one} <=> {word_two}')
#     return mirror_words

# def print_result(mirror_words):
#     if mirror_words:
#         print(f'The mirror words are:')
#         print(', '.join(mirror_words))
#     else:
#         print('No mirror words!')

# def main():
#     text = input()
#     mirror_words = find_mirror_words(text)
#     if mirror_words:
#         print(f'{len(mirror_words)} word pairs found!')
#         print_result(mirror_words)
#     else:
#         print('No word pairs found!')
#         print_result(mirror_words)

# if __name__ == '__main__':
#     main()
