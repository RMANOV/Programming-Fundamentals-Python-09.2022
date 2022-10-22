secret_message_list = input().split()


# Get item by item from the list
# check first, second and third number of the item, store them in a list, concatenate them and convert to int
# convert int to letter whit chr()
# insert the letter in a first list
# remove the first three numbers from the item
number = []
letter = []
digit_counter = 0
for item in secret_message_list:
    for symbol in item:
        if symbol.isdigit():
            number.append(symbol)
            digit_counter += 1
        else:
            letter.append(symbol)
    if digit_counter == 3:
        number = int("".join(number))
        number = chr(number)
        letter.insert(0, number)
        letter = "".join(letter)
        secret_message_list[secret_message_list.index(item)] = letter
        letter = []
        number = []
        digit_counter = 0
    elif digit_counter == 2:
        number = int("".join(number))
        number = chr(number)
        letter.insert(0, number)
        letter = "".join(letter)
        secret_message_list[secret_message_list.index(item)] = letter
        letter = []
        number = []
        digit_counter = 0
    elif digit_counter == 1:
        number = int("".join(number))
        number = chr(number)
        letter.insert(0, number)
        letter = "".join(letter)
        secret_message_list[secret_message_list.index(item)] = letter
        letter = []
        number = []
        digit_counter = 0

# swap the second and the last letter of each item
for item in secret_message_list:
    item = [char for char in item]  # convert string to list
    item[1], item[-1] = item[-1], item[1]  # swap the second and the last letter
    item = "".join(item)  # convert list to string
    secret_message_list[secret_message_list.index(item)] = item  # replace the item in the list

print(*secret_message_list)





           



    









# for item in item_list:     
#     number= [int(x) for x in item_list[:3] if x.isdigit()] # get first three numbers
#     letter.append(chr(number[0])) # convert to letter
#     item_list = [x for x in item_list if not x.isdigit()] # remove first three numbers
#     item_list.insert(0, letter[0]) # insert letter in the first position
#     letter = []
#     number = []
#     item = "".join(item_list)
#     print(item, end=" ")











    # for i in item:
    #     item_list = list(item)
    #     for i in range(3):
    #         if item_list[i].isdigit():
    #             number.append(item_list[i])
    #             number = int("".join(number))
    #             letter.append(chr(number))
    #             del item_list[0:3]
    #             item = "".join(item_list)
    #             number = []
    #             letter = []
    #         else:
    #             break

            # number = int("".join(number))
            # letter.append(chr(number))
            # del item_list[0:3]
            # item = "".join(item_list)
            # number = []
            # letter = []
            # break

        # if i.isdigit():
        #     number.append(i)
        #     item = item.replace(i, '')
        #     number = int(''.join(number))
        #     letter.append(chr(number))
        #     item[i] = letter
        #     number = []
        #     letter = []


# switch the second and last characters of each wordv
# get the item of above list and switch the second and last characters
# def switch_characters(get_secret_message):
#     for item in secret_message:
#         item[0],item[-1]=item[-1],item[0]
#     return secret_message


# print the result
# def print_result(switch_characters):
#     print("".join(switch_characters(get_secret_message(secret_message_list))))
