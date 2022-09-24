

n = int(input())
delim = "->"
digit_list = []
text_list = [int(x) for x in str(n)]
special_num = False

for i in range(len(text_list)):
    digit_list.__str__((text_list[i]))
    sum_list = sum(digit_list)
    print(sum_list, end=delim)

    # print(delim.join(str(x) for x in digit_list), end=" ")
    # if text_list[i] + text_list[i+1] == 7 or text_list[i] + text_list[i+1] == 11 or text_list[i] + text_list[i+1] == 5:
    # if sum == 7 or sum == 11 or sum == 5:
    #     special_num = True
    #     print(f"{text_list[i]}{delim}{special_num}")
    # else:
    #     special_num = False
    #     print(f"{text_list[i]}{delim}{special_num}")

# print(int(digit_list))







# print((digit_list[0]), end="")
