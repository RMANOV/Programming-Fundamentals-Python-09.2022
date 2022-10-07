

deck_of_cards = input().split()
number_shuffles = int(input())

for shuffle in range(number_shuffles):
    left_deck = deck_of_cards[:len(deck_of_cards) // 2]
    right_deck = deck_of_cards[len(deck_of_cards) // 2:]
    deck_of_cards = []
    for i in range(len(left_deck)):
        deck_of_cards.append(left_deck[i])
        deck_of_cards.append(right_deck[i])

print(deck_of_cards)