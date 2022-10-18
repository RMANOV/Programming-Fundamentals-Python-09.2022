

first_list = [x for x in input().split(", ")]
second_list = [x for x in input().split(", ")]

# result = [x for x in first_list if x in second_list]

list_of_matched_part_of_words = [x for x in first_list for y in second_list if x in y]
# substrings = [first for first in first_sequence if any(first in second for second in second_sequence)]

print(list_of_matched_part_of_words)