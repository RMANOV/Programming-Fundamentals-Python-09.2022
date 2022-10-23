

initial_deck_of_cards = input().split(', ')
number_of_commands = int(input())


for _ in range(number_of_commands):
    command = input().split(', ')
    if command[0] == 'Add':
        if command[1] in initial_deck_of_cards:
            print('Card is already in the deck')
        else:
            initial_deck_of_cards.append(command[1])
            print('Card successfully added')
    elif command[0] == 'Remove':
        if command[1] in initial_deck_of_cards:
            initial_deck_of_cards.remove(command[1])
            print('Card successfully removed')
        else:
            print('Card not found')
    elif command[0] == 'Remove At':
        if 0 <= int(command[1]) < len(initial_deck_of_cards):
            initial_deck_of_cards.pop(int(command[1]))
            print('Card successfully removed')
        else:
            print('Index out of range')
    elif command[0] == 'Insert':
        if 0 <= int(command[1]) < len(initial_deck_of_cards):
            if command[2] in initial_deck_of_cards:
                print('Card is already added')
            else:
                initial_deck_of_cards.insert(int(command[1]), command[2])
                print('Card successfully added')
        else:
            print('Index out of range')

print(*initial_deck_of_cards, sep=', ')