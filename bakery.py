

bakery = {}
elements = input().split(" ")

keys = elements[::2]
values = elements[1::2]

# add the keys and integer of the values to the dictionary
bakery.update(zip(keys, map(int, values)))


print(bakery)
