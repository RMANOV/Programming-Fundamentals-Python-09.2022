

f_string = input()
num_list = ()
print('[', end='')
count_i = 0

for i in range(len(f_string)):

    if f_string[i].isupper():

        count_i += 1

        if i == len(f_string) - 1:
            print(i, sep=', ', end='')
        else:
            print(i, sep=', ', end=', ')
print(']',sep=',')

#how to remove the last comma in the output?






#         num_list += (i,)
#         if i == len(num_list) - 0:
#             print(i, end=' ')
#         else:
#             print(f'{i},', end=' ')
# print(']', end='')

#how to convert list to string
#https://www.geeksforgeeks.org/python-convert-list-to-string/


# for i in range(len(f_string)):
#     if f_string[i].isupper():
#         num_list.append(i)
#         print(num_list)
#     else:
#         print(i)
# print()