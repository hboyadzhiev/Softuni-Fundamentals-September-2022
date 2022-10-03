deck_of_cards = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    final_deck = []
    middle = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle]
    right_part = deck_of_cards[middle::]
    for card_index in range(0, len(left_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
    deck_of_cards = final_deck
print(final_deck)