

n = int(input())
delim = "->"
text_list = [int(x) for x in str(n)]
special_num = False
digits_sum = 0
digits_list = []

for i in range(n):
    digits_list.append(i+1)
    digits_sum = sum(digits_list)

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:



        special_num = True

    
        print(f"{i+1}{delim}True")
        digits_sum = 0
    else:
        print(f"{i+1}{delim}False",sep="]")
        digits_sum = 0






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
