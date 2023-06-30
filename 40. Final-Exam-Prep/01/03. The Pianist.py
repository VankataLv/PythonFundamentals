init_pieces = int(input())
favorites = {}
for i in range(init_pieces):
    command = input()
    piece, *info = command.split("|")
    favorites[piece] = info
command = input()
while command != "Stop":
    tokens = command.split("|")
    if tokens[0] == "Add":  # 0 action | 1 piece | 2 composer | 3 key
        if tokens[1] in favorites:
            print(f"{tokens[1]} is already in the collection!")
        else:
            favorites[tokens[1]] = [tokens[2], tokens[3]]
            print(f"{tokens[1]} by {tokens[2]} in {tokens[3]} added to the collection!")
    elif tokens[0] == "Remove":  # 0 action | 1 piece
        if tokens[1] in favorites:
            print(f"Successfully removed {tokens[1]}!")
            favorites.pop(tokens[1])
        else:
            print(f"Invalid operation! {tokens[1]} does not exist in the collection.")
    elif tokens[0] == "ChangeKey":  # 0 action | 1 piece |2 new key
        if tokens[1] in favorites:
            print(f"Changed the key of {tokens[1]} to {tokens[2]}!")
            favorites[tokens[1]][1] = tokens[2]
        else:
            print(f"Invalid operation! {tokens[1]} does not exist in the collection.")
    command = input()
for key, value in favorites.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
