

elements = input().split(" ")
bakery = {}

keys = elements[::2]
values = elements[1::2]

bakery.update(zip(keys, map(int, values)))

searched_products = input().split(" ")

for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

# if searched_products[0] in bakery:
#     print(f"We have {bakery[searched_products[0]]} of {searched_products[0]} left")
# else:
#     print(f"Sorry, we don't have {searched_products[0]}")
    
# if searched_products[1] in bakery:
#     print(f"We have {bakery[searched_products[1]]} of {searched_products[1]} left")
# else:
#     print(f"Sorry, we don't have {searched_products[1]}")
    
