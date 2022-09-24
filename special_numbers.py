

n = int(input())
delim = "->"
text_list = [int(x) for x in str(n)]
special_num = False

for i in range(n):
    # if sum(text_list) == 5 or sum(text_list) == 7 or sum(text_list) == 11:
    if i == 7 or i == 11 or i == 5 or i + (i-n) == 5 or i + (i-n) == 7 or i + (i-n) == 11:

        special_num = True
        print(f"{i+1}{delim}True")
    else:
        print(f"{i+1}{delim}False",sep="]")






#     dlist.append(text_list[i])
#     if i < len(text_list) - 1:
#         dlist.append(delim)
    
# print("".join(str(x) for x in dlist))

# for i in range(len(text_list)):
#     digit_list.__str__((text_list[i]))
    # sum_list = sum(digit_list)
    # print(sum_list, end=delim)

    # print(delim.join(str(x) for x in digit_list), end=" ")
    # if text_list[i] + text_list[i+1] == 7 or text_list[i] + text_list[i+1] == 11 or text_list[i] + text_list[i+1] == 5:
    # if sum == 7 or sum == 11 or sum == 5:
    #     special_num = True
    #     print(f"{text_list[i]}{delim}{special_num}")
    # else:
    #     special_num = False
    #     print(f"{text_list[i]}{delim}{special_num}")



# print((digit_list[0]), end="")
