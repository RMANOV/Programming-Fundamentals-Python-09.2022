
# Shadowmourne" - requires 250 Shards
# Valanyr" - requires 250 Fragments
# Dragonwrath" - requires 250 Motes

items_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}
initial_list =input().split()

while True:
    for i in range(0, len(initial_list), 2):
        if initial_list[i + 1].lower() in items_dict:
            items_dict[initial_list[i + 1].lower()] += int(initial_list[i])
        else:
            junk_dict[initial_list[i + 1].lower()] = junk_dict.get(initial_list[i + 1].lower(), 0) + int(initial_list[i])
            
        if items_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            for key, value in sorted(junk_dict.items(), key=lambda x: (-x[1], x[0])):
                print(f"{key}: {value}")
            break
        elif items_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            for key, value in sorted(junk_dict.items(), key=lambda x: (-x[1], x[0])):
                print(f"{key}: {value}")
            break              
        elif items_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            for key, value in sorted(junk_dict.items(), key=lambda x: (-x[1], x[0])):
                print(f"{key}: {value}")
            break
            
    if items_dict["shards"] >= 250 or items_dict["fragments"] >= 250 or items_dict["motes"] >= 250:
        break
    
    initial_list = input().split()
    
# for key, value in sorted(items_dict.items(), key=lambda x: (-x[1], x[0])):
    
              
              
              
              
              
              
              
    #     key = initial_list[i + 1].lower()
    #     value = int(initial_list[i])
    #     if key in items_dict:
    #         items_dict[key] += value
    #     else:
    #         items_dict[key] = value

    #     if items_dict[key] >= 250:
    #         if key == "shards":
    #             print("Shadowmourne obtained!")
    #             print(*[f"{k}: {v}" for k, v in sorted(items_dict.items(), key=lambda x: (-x[1], x[0]))], sep='')
    #             print(*[f"{k}: {v}" for k, v in sorted(items_dict.items(), key=lambda x: (-x[1], x[0])) if k != "shards" and k != "fragments" and k != "motes"], sep='')
    #             break
    #         elif key == "fragments":
    #             print("Valanyr obtained!")
    #             print(*[f"{k}: {v}" for k, v in sorted(items_dict.items(), key=lambda x: (-x[1], x[0]))], sep='')
    #             print(*[f"{k}: {v}" for k, v in sorted(items_dict.items(), key=lambda x: (-x[1], x[0])) if k != "shards" and k != "fragments" and k != "motes"], sep='')
    #             break
    #         elif key == "motes":
    #             print("Dragonwrath obtained!")
    #             print(*[f"{k}: {v}" for k, v in sorted(items_dict.items(), key=lambda x: (-x[1], x[0]))], sep='')
    #             print(*[f"{k}: {v}" for k, v in sorted(items_dict.items(), key=lambda x: (-x[1], x[0])) if k != "shards" and k != "fragments" and k != "motes"], sep='')
    #             break
    #         # items_dict[key] -= 250
    #         break
    # else:
    #     initial_list = input().split()
    #     continue
    # break


# for i in range(0, len(initial_list), 2):
#     quantity = int(initial_list[i])
#     item = initial_list[i + 1]
#     if item in items_dict:
#         items_dict[item] += quantity
#         if items_dict[item] >= 250:
#             if item == "shards":
#                 print("Shadowmourne obtained!")
#             elif item == "fragments":
#                 print("Valanyr obtained!")
#             elif item == "motes":
#                 print("Dragonwrath obtained!")
#             break
#     else:
#         items_dict[item] = quantity
       
# junk_dict = {k: v for k, v in items_dict.items() if v < 250}
# items_dict = {k: v for k, v in items_dict.items() if v >= 250}
# print(*[f"{k}: {v}" for k, v in sorted(items_dict.items(), key=lambda x: (-x[1], x[0]))], sep="'n")
