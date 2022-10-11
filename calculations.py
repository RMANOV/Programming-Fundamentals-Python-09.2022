
def add_operation(a, b):
    return a + b
def sub_operation(a, b):
    return a - b
def mul_operation(a, b):
    return a * b
def div_operation(a, b):
    return a / b





operation = input()
first_number = int(input())
second_number = int(input())


if operation == "+" or operation == "add":
    print(int(add_operation(first_number, second_number)))
elif operation == "-" or operation == "subtract":
    print(int(sub_operation(first_number, second_number)))
elif operation == "*" or operation == "multiply":
    print(int(mul_operation(first_number, second_number)))
elif operation == "/" or operation == "divide":
    print(int(div_operation(first_number, second_number)))
