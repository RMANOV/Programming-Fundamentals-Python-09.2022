

number_of_orders = int(input())
current_order = []
orders = []
for i in range(number_of_orders+1):
    for i in range(3):
        if not i == 0 or i < 0:
            current_order.append((input()))
        else:
            continue
    current_cost = float(current_order[0]) * int(current_order[1]) * int(current_order[2])
    orders.append(current_cost)
    print(f"The price for the coffee is: ${current_cost}")
    current_order = []

total_orders = sum(orders)
print("Total: ${total_orders:.2f}")








































# current_order = 0
# total_orders = 0

# for i in range(number_of_orders):
#     price_per_capsule  = float(input())
#     days = int(input())
#     capsules_count = int(input())
#     if price_per_capsule <= 0 or days <= 0 or capsules_count <= 0:
#         continue
#     current_order = (days * capsules_count) * price_per_capsule
#     print(f"The price for the coffee is: ${current_order:.2f}")
#     total_orders += current_order

# print(f"Total: ${total_orders:.2f}")
