

# On the first line of the input, you will receive the concealed message. 
# After that, until the "Reveal" command is given, you will receive strings with instructions for different operations that need to be performed 
# upon the concealed message to interpret it and reveal its actual content. 
# There are several types of instructions, split by ":|:"
# •	"InsertSpace:|:{index}":
# o	Inserts a single space at the given index. The given index will always be valid.
# •	"Reverse:|:{substring}":
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message. 
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
# •	"ChangeAll:|:{substring}:|:{replacement}":
# o	Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by ":|:".
# Output
# •	After each set of instructions, print the resulting string. 
# •	After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"

encrypted_message = ''

def decrypt_message(message):
    global encrypted_message
    encrypted_message = message
    
    
def main():
    global encrypted_message
    try:
        decrypt_message(input())
        command = input()
        while command != 'Reveal':
            command = command.split(':|:')
            if command[0] == 'InsertSpace':
                encrypted_message = encrypted_message[:int(command[1])] + ' ' + encrypted_message[int(command[1]):]
                print(encrypted_message)
            elif command[0] == 'Reverse':
                if command[1] in encrypted_message:
                    encrypted_message = encrypted_message.replace(command[1], '', 1)
                    encrypted_message += command[1][::-1]
                    print(encrypted_message)
                else:
                    print('error')
            elif command[0] == 'ChangeAll':
                encrypted_message = encrypted_message.replace(command[1], command[2])
                print(encrypted_message)
            command = input()
        print(f'You have a new text message: {encrypted_message}')

    except Exception as e:
        print(e)
        print('error')

if __name__ == '__main__':
    main()
