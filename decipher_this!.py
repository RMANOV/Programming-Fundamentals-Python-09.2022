secret_message_list = input().split()


# Get item by item from the list
# check first, second and third number of the item, store them in a list, concatenate them and convert to int
#convert int to letter whit chr()
#insert the letter in a first list
#remove the first three numbers from the item

secret_message = [x for x in secret_message_list]
number = []
letter = []
for item in secret_message:
    for i in word:
        if i.isdigit():
            number.append(i)
        else:
            letter.append(i)
number = int(''.join(number))
letter = chr(number)
secret_message.insert(0, letter)
secret_message.remove(number)
print

# switch the second and last characters of each wordv
# get the item of above list and switch the second and last characters
# def switch_characters(get_secret_message):
#     for item in secret_message:
#         item[0],item[-1]=item[-1],item[0]
#     return secret_message


# print the result
# def print_result(switch_characters):
#     print("".join(switch_characters(get_secret_message(secret_message_list))))
