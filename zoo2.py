

my_list = []

for i in range(3):
    my_list.append(input())

my_list = [i.strip() for i in my_list]
print(my_list)
