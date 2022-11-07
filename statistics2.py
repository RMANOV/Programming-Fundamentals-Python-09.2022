

class Bakery_statistics:
    
    bakery = {}
    
    def __init__(self, command):
        self.command = command
        
        while self.command[0] != "statistics":
            
            if self.command[0] in self.bakery:
                self.bakery[self.command[0]] += int(self.command[1])
            else:
                self.bakery[self.command[0]] = int(self.command[1])
                
            self.command = input().split(": ")
            
        print("Products in stock:")
        for key, value in self.bakery.items():
            print(f"- {key}: {value}")
        
            
        print(f"Total Products: {len(self.bakery)}")
        print(f"Total Quantity: {sum(self.bakery.values())}")





















# bakery = {}

# command = input().split(": ")
# while command[0] != "statistics":

#     if command[0] in bakery:
#         bakery[command[0]] += int(command[1])
#     else:
#         bakery[command[0]] = int(command[1])

#         command = input().split(": ")

# print("Products in stock:")
# for key, value in bakery.items():
#     print(f"- {key}: {value}")

# # print("Products in stock:")
# # for key, value in bakery.items():
# #     print(f"- {key}: {value}")

# print(f"Total Products: {len(bakery)}")
# print(f"Total Quantity: {sum(bakery.values())}")

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
