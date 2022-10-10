
def add_operation(a, b):
    return a + b
def sub_operation(a, b):
    return a - b
def mul_operation(a, b):
    return a * b
def div_operation(a, b):
    return a / b






first_number = int(input())
second_number = int(input())
operation = input()

if operation == "+" or operation == "add":
    print(add_operation(first_number, second_number))
elif operation == "-" or operation == "substract":
    print(sub_operation(first_number, second_number))
elif operation == "*" or operation == "multiply":
    print(mul_operation(first_number, second_number))
elif operation == "/" or operation == "divide":
    print(div_operation(first_number, second_number))
