

f_number = input()

for i in range(len(f_number)):


    last_digit = int(f_number[-i])
    digit_list = [int(i) for i in f_number]
    print(max(digit_list), end="")
    digit_list.remove(max(digit_list))
    print(max(digit_list), end="")




  

print()
    # digit_list.append(last_digit)
    # f_number = f_number[:-1]
    # if last_digit > int(f_number[i+1:i+2]):
    #     print(last_digit)
    # else:
    #     print(int(f_number[i+1:i+2]))
    #     break










    # digits = int(f_number[i+1:(i-2)])

    # print(last_digit, digits)

    # if last_digit > digits:
    #     print(last_digit, end="")        
    # else:
    #     print(digits, end="")
        
    #     digits = 0
    #     last_digit = 0  

    # print(len(f_number))


    # digital = int(f_number)
    # print(digital)
    # print(digital*2)

    # if digital[i] > digital[i+1]:
    #     print(digital[i])
    # else:
    #     print(digital[i+1])
    
