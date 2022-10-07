card_string = input().split()
card_list = []
card_list.append(card_string)

number_shuffles = int(input())

for shuffle in range(number_shuffles):
    final_deck = []
    midle_of_deck = int(len(card_list[0]) // 2)
    left_part = card_list[0:midle_of_deck]
    right_part = card_list[midle_of_deck::]
    for i in range(len(left_part)):
        final_deck.append(left_part[i])
        final_deck.append(right_part[i])
    card_list = final_deck
    print(final_deck)