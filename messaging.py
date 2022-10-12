

number_list = [int(i) for i in input().split()]
digit_list = []

for i in number_list:
    if i not in digit_list:
        digit_list.append(int(i))



print(digit_list)