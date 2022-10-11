

def palindrome_integers(numbers):
    for number in numbers:
        if number == int(str(number)[::-1]):
            print('True')
        else:
            print('False')



initial_list = input().split(", ")
initial_list = [int(i) for i in initial_list]


palindrome_integers(initial_list)