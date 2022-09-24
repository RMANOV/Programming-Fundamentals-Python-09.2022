

n = int(input())
delim = "->"
digit_list = []
text_list = [int(x) for x in str(n)]
special_num = False
# for i in range (len(str(n))):
#     digit_list.append(int(str(n)[i]))
    


for i in range(len(text_list)):
    if text_list[i] + text_list[i+1] == 7 or text_list[i] + text_list[i+1] == 11 or text_list[i] + text_list[i+1] == 5:
        special_num = True
        
        break









print((digit_list[0]), end="")
