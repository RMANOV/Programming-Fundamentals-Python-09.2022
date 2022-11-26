

# You are a pianist, and you like to keep a list of your favorite piano pieces. 
# Create a program to help you organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have. 
# On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
# •	"Add|{piece}|{composer}|{key}":
# o	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# •	"Remove|{piece}":
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	"ChangeKey|{piece}|{new key}":
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection
# •	For each piece, you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above until the command "Stop".
# Output:
# Hungarian Rhapsody No.2 by Liszt in C# Minor added to the collection!
# Fur Elise is already in the collection!
# Successfully removed Clair de Lune!
# Changed the key of Moonlight Sonata to C# Major!
# Fur Elise -> Composer: Beethoven, Key: A Minor
# Moonlight Sonata -> Composer: Beethoven, Key: C# Major
# Sonata No.2 -> Composer: Chopin, Key: B Minor
# Hungarian Rhapsody No.2 -> Composer: Liszt, Key: C# Minor

def add_piece(piece, composer, key, pieces):
    if piece in pieces:
        print(f'{piece} is already in the collection!')
    else:
        pieces[piece] = {'composer': composer, 'key': key}
        print(f'{piece} by {composer} in {key} added to the collection!')

def remove_piece(piece, pieces):
    if piece not in pieces:
        print(f('Invalid operation! {piece} does not exist in the collection.'))
    else:
        del pieces[piece]
        print(f'{piece} by {pieces["composer"]} in {pieces["key"]} removed from the collection!')

def change_key(piece, new_key, pieces):
    if piece not in pieces:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    else:
        pieces[piece]['key'] = new_key
        print(f'Changed the key of {piece} to {new_key}!')

def change_composer(piece, new_composer, pieces):
    if piece not in pieces:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    else:
        pieces[piece]['composer'] = new_composer
        print(f'Changed the composer of {piece} to {new_composer}!')

def print_pieces(pieces):
    for piece in pieces:
        print(f'{piece} -> Composer: {pieces[piece]["composer"]}, Key: {pieces[piece]["key"]}')

pieces = {}

def main():
    print_pieces(pieces)
    while True:
        command = input()
        if command == 'Stop':
            break
        command = command.split('|')
        if command[0] == 'Add':
            add_piece(command[1], command[2], command[3], pieces)
        elif command[0] == 'Remove':
            remove_piece(command[1], pieces)
        elif command[0] == 'ChangeKey':
            change_key(command[1], command[2], pieces)
        elif command[0] == 'ChangeComposer':
            change_composer(command[1], command[2], pieces)
        else:
            print(f'Invalid command! {command}')

if __name__ == '__main__':
    main()
    print()