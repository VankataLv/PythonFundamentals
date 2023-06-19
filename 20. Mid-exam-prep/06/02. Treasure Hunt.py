initial_loot = input().split("|")
command = input()
removed_items = []

while command != "Yohoho!":
    if command[:4] == "Loot":
        current_loot = list(command.split(" "))         # list because we do not know how many items are there
        current_loot.remove("Loot")
        for item in current_loot:
            if item in initial_loot:
                pass
            else:
                initial_loot.insert(0, item)
        current_loot = []                               # reinitialize the current loot list
    elif command[:4] == "Drop":
        action, index = command.split(" ")
        index = int(index)
        if index < len(initial_loot):
            item_to_move = initial_loot[index]          # save the item
            initial_loot.remove(item_to_move)
            initial_loot.append(item_to_move)
        else:
            command = input()
            continue
    elif command[:5] == "Steal":
        action, index = command.split(" ")
        index = int(index)
        if index > len(initial_loot):                   # more items to remove than existing in the list
            print(", ".join(initial_loot))
            initial_loot.clear()
        else:
            for _ in range(index):
                removed_items.insert(0, initial_loot[-1])
                initial_loot.pop()
            print(", ".join(removed_items))
        removed_items.clear()
    command = input()

if len(initial_loot) == 0:                              # in case the list is empty
    print("Failed treasure hunt.")
    quit()

all_items = 0
for el in initial_loot:
    all_items += len(el)
all_items /= len(initial_loot)
print(f"Average treasure gain: {all_items:.2f} pirate credits.")
