

# On the first line, you will receive a sequence of numbers separated by a single space. 
# On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string. 
# Each char the program adds to the message should be found by its index. 
# The index you are looking for is the sum of a number's digits from the sequence. 
# If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index). 
# When you find a char, you should add it to the message and remove it from the string. 
# It means that for the following index, the text will be with one character less.

number_list = [int(i) for i in input().split()]
encrypted_message = input()

for i in number_list:
    current_sum = 0
    while i > 0:
        if current_sum > len(encrypted_message):
            current_sum = current_sum % len(encrypted_message)
            
        current_sum += i % 10
        i = i // 10
        
        if current_sum > len(encrypted_message):
            current_sum -= len(encrypted_message)
            
    print(encrypted_message[current_sum], end="")
    encrypted_message = encrypted_message[:current_sum] + encrypted_message[current_sum + 1:]





# initial_sequence = [int(i) for i in input().split()]
# initial_text = input()

# for i in initial_sequence:
#     current_sum = 0

#     while i > 0:
#         current_sum += i % 10
#         i = i // 10
        
#         if current_sum > len(initial_text):
#             current_sum -= len(initial_text)
            
#     print(initial_text[current_sum], end="")
#     initial_text = initial_text[:current_sum] + initial_text[current_sum + 1:]



# def get_sum_of_digits(number):
#     current_sum = 0
#     while number > 0:
#         current_sum += number % 10 
#         number = number // 10 # integer division
#     return current_sum

# def get_index(number_list, messaging):
#     digit_list = []
#     for i in number_list:
#         current_sum = 0
#         while i > 0:
#             current_sum += i % 10
#             i = i // 10
#             digit_list.append(current_sum)
#     return digit_list

# def get_message(digit_list, messaging):
#     message = ""
#     for i in digit_list:
#         if len(messaging) <= 0:
#             i=0
#         if i >= len(messaging):
#             i = i % len(messaging)
#         message += messaging[i]
#         messaging = messaging[i + 1:]
#     return message

# def main():
#     number_list = [int(i) for i in input().split()]
#     messaging = input()
#     digit_list = get_index(number_list, messaging)
#     message = get_message(digit_list, messaging)
#     print(message)

# main()