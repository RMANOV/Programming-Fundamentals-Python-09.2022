

products = {}
initial_list = input().split()

while initial_list[0] != "buy":
    product = initial_list[0]
    price = float(initial_list[1])
    quantity = int(initial_list[2])
    if product not in products:
        products[product] = [price, quantity]
    else:
        products[product][0] = price
        products[product][1] += quantity
    initial_list = input().split()
    
for key, value in products.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")

