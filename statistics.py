

bakery = {input().split()[0]: int(input()) for _ in range(int(input()))}

while command!= "statistics"

    command = input().split(": ")
    if command[0] not in bakery:
        keys = command[0]
        values = int(command[1])
        bakery[keys] = values
    else:
        bakery[keys] += values
        
print("Products in stock:")
for key, value in bakery.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(bakery)}")
    
    
    
        
    
        
        
    
