# Input
# •	The possible commands are:
# o	"Ready"
# o	"Add {cardName}"
# o	"Insert {cardName} {index}"
# o	"Remove {cardName}"
# o	"Swap {cardName1} {cardName2}"
# o	"Shuffle deck"
# Output
# •	The possible outputs are:
# o	"{cardName1} - {cardName2}"
# o	"Card not found."
# o	"Error!"

initial_deck = input().split(":")

while True:
    command = input().split()
    if command[0] == "Ready":
        break
    elif command[0] == "Add":
        if command[1] not in initial_deck:
            initial_deck.append(command[1])
        else:
            print("Card is already bought")
    elif command[0] == "Insert":
        if command[1] not in initial_deck:
            print("Error!")
        else:
            initial_deck.insert(int(command[2]), command[1])
    elif command[0] == "Remove":
        if command[1] not in initial_deck:
            print("Card not found.")
        else:
            initial_deck.remove(command[1])
    elif command[0] == "Swap":
        if command[1] not in initial_deck or command[2] not in initial_deck:
            print("Error!")
        else:
            first_card = initial_deck.index(command[1])
            second_card = initial_deck.index(command[2])
            initial_deck[first_card], initial_deck[second_card] = initial_deck[second_card], initial_deck[first_card]
    elif command[0] == "Shuffle":
        initial_deck.reverse()

print(" ".join(initial_deck))