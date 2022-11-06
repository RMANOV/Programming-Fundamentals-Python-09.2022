

bakery = {}

command = input().split(": ")
while command[0] != "statistics":
    
    if command[0] in bakery:
        bakery[command[0]] += int(command[1])
    else:
        bakery[command[0]] = int(command[1])
        
        command = input().split(": ")
        
print("Products in stock:")
for key, value in bakery.items():
    print(f"- {key}: {value}")
    


print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")

      
        
        

    
    
        
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
