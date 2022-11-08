

initial_list = [input().split(",")]
ascii_dict = {}

for  i in initial_list[0]:
    ascii_dict[i] = ord(i)
    
    
print(ascii_dict)

# ascii_dict = {initial_list[0][i]: ord(initial_list[0][i]) for i in range(len(initial_list[0]))}
# print(ascii_dict)