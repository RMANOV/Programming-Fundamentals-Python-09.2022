

check_number = int(input())
is_prime = True

for i in range(2, check_number):

    if check_number % i == 0:
        is_prime = False
        print("False")
        break
    else:
        # if check_number == 81:
        #         print("False")
        #         break
        is_prime = True
        print("True")
        break
