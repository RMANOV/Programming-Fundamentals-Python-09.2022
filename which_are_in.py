

first_list = [x for x in input().split(", ")]
second_list = [x for x in input().split(", ")]

list_of_matched_part_of_words = []

# result = [x for x in first_list if x in second_list]

list_of_matched_part_of_words = [x for x in first_list for y in second_list if x in y]
# substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]

# for first in first_list:
#     for second in second_list:
#         if first in second:
#             list_of_matched_part_of_words.append(first)

print(list_of_matched_part_of_words)
