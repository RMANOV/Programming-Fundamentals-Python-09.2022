

final_number = (input().strip())
digit_list = [int(x) for x in str(final_number)]
even_list = [i for i in digit_list if i % 2 == 0]
odd_list = [i for i in digit_list if i % 2 != 0]




even_sum = sum(even_list)
odd_sum = sum(odd_list)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")