inventory = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
legendary = False
while not legendary:
    farming = input().split(" ")  # [0-quantity, 1-material, 2-qty, 3-mat]
    for el_i in range(0, len(farming), 2):  # el_i 0,2,4,6,8
        value = int(farming[el_i])
        key = farming[el_i + 1].lower()
        if key not in inventory.keys():
            inventory[key] = 0
        inventory[key] += value
        if inventory["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary = True
            inventory["shards"] -= 250
        elif inventory["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary = True
            inventory["fragments"] -= 250
        elif inventory["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary = True
            inventory["motes"] -= 250
        if legendary:
            break

for key, value in inventory.items():
    print(f"{key}: {value}")

# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards

# 123 silver 6 shards 8 shards 5 motes
# 9 fangs 75 motes 103 MOTES 8 Shards
# 86 Motes 7 stones 19 silver
