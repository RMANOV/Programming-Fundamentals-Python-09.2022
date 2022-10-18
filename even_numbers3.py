

initial_list_of_numbers = [int(i) for i in input().split(", ")]
list_of_indexes_of_even_numbers = [i for i in range(len(initial_list_of_numbers)) if initial_list_of_numbers[i] % 2 == 0]

print(list_of_indexes_of_even_numbers)