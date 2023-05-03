card_input = input()
original_deck = card_input.split(" ")
faro_shuffles = int(input())
top_card = original_deck[0]
bottom_card = original_deck[-1]
original_deck.pop(0)
original_deck.pop(-1)
for shuffles in range(faro_shuffles):
    original_deck.reverse()
original_deck.insert(0, top_card)
original_deck.append(bottom_card)
print(original_deck)
