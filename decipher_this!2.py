secret_message_list = input().split()


# Get item by item from the list
# check first, second and third number of the item, store them in a list, concatenate them and convert to int
# convert int to letter whit chr()
# insert the letter in a first list
# remove the first three numbers from the item

secret_message = [x for x in secret_message_list]
number = []
letter = []
for item in secret_message:
    item_list =[x for x in item]
    number= [int(x) for x in item_list[:3] if x.isdigit()] # get first three numbers
    letter.append(chr(number[0])) # convert to letter
    item_list = [x for x in item_list if not x.isdigit()] # remove first three numbers
    item_list.insert(0, letter[0]) # insert letter in the first position
    letter = []
    number = []
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
print(secret_message)

# switch the second and last characters of each wordv
# get the item of above list and switch the second and last characters
# def switch_characters(get_secret_message):
#     for item in secret_message:
#         item[0],item[-1]=item[-1],item[0]
#     return secret_message


# print the result
# def print_result(switch_characters):
#     print("".join(switch_characters(get_secret_message(secret_message_list))))
