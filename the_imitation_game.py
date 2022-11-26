

# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code. 
# Your job is to create a program to crack the codes. 
# On the first line of the input, you will receive the encrypted message. 
# After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its true content. 
# There are several types of instructions, split by '|'
# •	"Move {number of letters}":
# o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
# o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
# o	Changes all occurrences of the given substring with the replacement text
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by '|' .
# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"

encrypted_message = [x for x in input()]

command = input().split('|')

while command[0] != 'Decode':
    if command[0] == 'Move':
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        # encrypted_message.insert(index, value)
        # encrypted_message = encrypted_message[:index] + [value] + encrypted_message[index:]
        # value = list(value)
        # encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
        # for index, value in enumerate(encrypted_message):
        #     encrypted_message[index] = value
        lenght = len(value)
        for i in range(lenght):
            encrypted_message.insert(index + i, value[i])
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        encrypted_message = ''.join(encrypted_message).replace(substring, replacement)
    command = input().split('|')

encrypted_message = ''.join(encrypted_message)
print(f'The decrypted message is: {encrypted_message}')
