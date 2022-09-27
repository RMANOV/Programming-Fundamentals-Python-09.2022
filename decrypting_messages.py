

key_decryptor = int(input())
number_lines = int(input())
encrypted_message = input()


for i in range(number_lines):
    
    decrypted_message = []
    for letter in encrypted_message:
        # decrypted_message += chr(ord(letter) + key_decryptor)
        decrypted_message.append(chr(ord(letter) + key_decryptor))

print(*decrypted_message, sep="")