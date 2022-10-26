

number_for_check_if_prime = int(input())
is_prime = True

for i in range(2, number_for_check_if_prime):
    if number_for_check_if_prime % i == 0:
        is_prime = False
        print("False")
        break

if is_prime:
    print("True")