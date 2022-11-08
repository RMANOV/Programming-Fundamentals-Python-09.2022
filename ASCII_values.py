

initial_list = input().split(", ")


ascii_dict = {key : ord(key) for key in initial_list}

print(ascii_dict)

# ascii_dict = {initial_list[0][i]: ord(initial_list[0][i]) for i in range(len(initial_list[0]))}
# print(ascii_dict)