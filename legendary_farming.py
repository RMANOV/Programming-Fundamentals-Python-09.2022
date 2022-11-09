
# Shadowmourne" - requires 250 Shards
# Valanyr" - requires 250 Fragments
# Dragonwrath" - requires 250 Motes

items_dict = {}
initial_list =input().split()

for i in range(0, len(initial_list), 2):
    quantity = int(initial_list[i])
    item = initial_list[i + 1]
    if item in items_dict:
        items_dict[item] += quantity
        if items_dict[item] >= 250:
            if item == "shards":
                print("Shadowmourne obtained!")
            elif item == "fragments":
                print("Valanyr obtained!")
            elif item == "motes":
                print("Dragonwrath obtained!")
            break
    else:
        items_dict[item] = quantity
       
junk_dict = {k: v for k, v in items_dict.items() if v < 250}
items_dict = {k: v for k, v in items_dict.items() if v >= 250}
print(*[f"{k}: {v}" for k, v in sorted(items_dict.items(), key=lambda x: (-x[1], x[0]))], sep="'n")
