

number_list = [int(i) for i in input().split()]
digit_list = []
messaging = input()

for i in number_list:
current_sum = 0
while i > 0:
current_sum += i % 10
i = i // 10
digit_list.append(current_sum)

for i in digit_list:
print(messaging[i], end="")
messaging = messaging[i + 1:]




# def get_sum_of_digits(number):
#     current_sum = 0
#     while number > 0:
#         current_sum += number % 10 
#         number = number // 10 # integer division
#     return current_sum