

f_string = input()
num_list = ()
print('[', end='')

for i in range(len(f_string)):
    if f_string[i].isupper():
        num_list += (i,)
        if i == len(num_list) - 0:
            print(i, end=' ')
        else:
            print(f'{i},', end=' ')
print(']', end='')

#how to convert list to string
#https://www.geeksforgeeks.org/python-convert-list-to-string/


# for i in range(len(f_string)):
#     if f_string[i].isupper():
#         num_list.append(i)
#         print(num_list)
#     else:
#         print(i)
# print()