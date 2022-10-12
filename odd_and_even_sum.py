

def odd_and_even_sum(n):
    odd_sum = 0
    even_sum = 0

    for int(number) in initial_list:
        if int(number) % 2 == 0:
            even_sum += int(number)
        else:
            odd_sum += number
   



initial_string = input()
initial_list = [initial_string[i] for i in range(len(initial_string))]

print(f'"Odd sum = {odd_sum()}, Even sum = {even_sum}"')