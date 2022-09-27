

key_decryptor = int(input())
number_lines = int(input())
decrypted_message = []


for i in range(number_lines):
    encrypted_message = input()
    for letter in encrypted_message:
        # decrypted_message += chr(ord(letter) + key_decryptor)
        decrypted_message.append(chr(ord(letter) + key_decryptor))
print(*decrypted_message, sep="")