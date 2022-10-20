

secret_message_list = input().split()

# switch the second and last characters of each word
for i in range(len(secret_message_list)):
    word = secret_message_list[i]
    secret_message_list[i] = word[0] + word[-1] + word[2:-1] + word[1]

    #replace first number with asci code
    for j in range(len(secret_message_list[i])):
        if secret_message_list[i][j].isdigit():
            secret_message_list[i] = secret_message_list[i][:j] + chr(int(secret_message_list[i][j]) + 33) + secret_message_list[i][j + 1:]
            break

# print the result
print(" ".join(secret_message_list))