deck_cards = input().split(" ")
faro_shuffles = int(input())
middle_deck = int(len(deck_cards) / 2)
current_deck = list()

for shuffle in range(faro_shuffles):
    current_deck = list()                   # Every for loop iteration you re-initialize the current list
    top_deck = deck_cards[:middle_deck]     # 0, 1, 2
    bottom_deck = deck_cards[middle_deck:]  # 3, 4, 5

    for card_index in range(middle_deck):     # 0, 1, 2
        current_deck.append(top_deck[card_index])
        current_deck.append(bottom_deck[card_index])
    deck_cards = current_deck

print(deck_cards)

