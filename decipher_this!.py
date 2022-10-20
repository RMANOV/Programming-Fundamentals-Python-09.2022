

secret_message_list = input().split()


# Get item by item from the list
# check first, second and third number of the item, store them in a list, concatenate them and convert to int
#convert int to letter whit chr()
#insert the letter in a first list
#remove the first three numbers from the item
def get_secret_message(secret_message_list):
    secret_message = []
    for item in secret_message_list:
        first_number = item[0]
        second_number = item[1]
        third_number = item[2]
        numbers = first_number + second_number + third_number
        numbers = int(numbers)
        letter = chr(numbers)
        secret_message.insert(0, letter)
        # item = item[3:]
    return secret_message





# switch the second and last characters of each word
# get the item of above list and switch the second and last characters
def switch_characters(secret_message):
    for item in secret_message:
        item[0],item[-1]=item[-1],item[0]
    return secret_message



# print the result
def print_result(secret_message):
    print("".join(secret_message))
