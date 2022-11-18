

key_decryptor = input().split()
while True:
    message = input()
    if message == 'find':
        break
    decrypted_message = ''
    for i in range(len(message)):
        decrypted_message += chr(ord(message[i]) - int(key_decryptor[i % len(key_decryptor)]))
    type_of_treasure = decrypted_message[decrypted_message.index('&') + 1: decrypted_message.rindex('&')]
    coordinates = decrypted_message[decrypted_message.index('<') + 1: decrypted_message.rindex('>')]
    print(f"Found {type_of_treasure} at {coordinates}")