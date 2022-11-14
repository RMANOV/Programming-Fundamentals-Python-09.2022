

bakery = {}
command = input()

while command != "statistics":
    key, value = command.split(": ")
    if key not in bakery.keys():
        bakery[key] = 0
    bakery[key] += int(value)
    command = input()
    
print("Products in stock:")
print(*[f"- {product}: {quantity}" for product, quantity in bakery.items()], sep="\n")

print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")

# Path: statistics.py
      












# Path: statistics.py

#     if command[0] not in bakery:
#         keys = command[0]
#         values = int(command[1])
#         bakery[keys] = values
#     else:
#         bakery[keys] += values
        
#     command = input().split(": ")
    
# print("Products in stock:")
# for key, value in bakery.items():
#     print(f"- {key}: {value}")

# print(f"Total Products: {len(bakery)}")
# print(f"Total Quantity: {sum(bakery.values())}")
