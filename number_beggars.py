

money_string = input().split(", ")
money_list = []

for i in money_string:
    money_list.append(int(i))

number_of_beggars = int(input())

final_sums = []
starting_index = 0

while starting_index < number_of_beggars:
    sum_of_current_beggars = 0
    for i in range(starting_index, len(money_list), number_of_beggars):
        sum_of_current_beggars += money_list[i]
    final_sums.append(sum_of_current_beggars)
    starting_index += 1

print(final_sums)