
n = int(input())
delim = " -> "
text_list = [int(x) for x in str(n)]
special_num = False
digits_sum = 0
digits_list = []




for i in range(1,n+1):

    for j in range(len(text_list)):
        digits_sum += text_list[j]
        digits_list.append(text_list[j])

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        special_num = True
    else:
        special_num = False

    if special_num:
        print(str(i) + delim + "True")
    else:
        print(str(i) + delim + "False")

    text_list = [int(x) for x in str(i+1)]
    digits_sum = 0
    digits_list = []



    
    # if i = 5 or i = 7 or i = 11:
    #     special_num = True
    # # if i % 5 == 0 or i % 7 == 0 or i % 11 == 0:
    # #               special_num = True True

    #     print(f"{i}{delim}True")
    # else:
    #     special_num = False
    #     print(f"{i}{delim}False")


   


 # digits_list.append(i+1)
    # # print(digits_list[i:i+1], end=delim)
    # digits_sum =[digits_list[i:i+1][0]]
    # Sum = sum(digits_sum)


    # digits_list.append(i+1)
    # digits_sum = sum(digits_list)

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
