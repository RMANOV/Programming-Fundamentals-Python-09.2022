

first_number = int(input())
second_number = int(input())

c = first_number
first_number = second_number
second_number = c

print(f"Before:\na = {second_number}\nb = {first_number}")
print(f"After:\na = {first_number}\nb = {second_number}")
