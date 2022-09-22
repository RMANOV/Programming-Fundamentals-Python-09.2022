

f_number = input()

for i in range(len(f_number)):
    digits =int(f_number[i+1:])
    last_digit = int(f_number[i])         
    if last_digit > digits:
        print(last_digit), print(digits)
        break

    # print(len(f_number))


    # digital = int(f_number)
    # print(digital)
    # print(digital*2)

    # if digital[i] > digital[i+1]:
    #     print(digital[i])
    # else:
    #     print(digital[i+1])
    pass
