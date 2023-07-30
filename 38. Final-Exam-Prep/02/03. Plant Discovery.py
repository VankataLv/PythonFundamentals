n = int(input())
catalogue = {}
avg_rat_cur_plant = 0
for i in range(n):
    key, rarity = input().split("<->")
    catalogue[key] = [int(rarity)]         # key: [0 rarity, 1 + infinity ratings]
command = input()
while command != "Exhibition":
    action, info = command.split(": ")   # action: info -> [0, 1]
    if action == "Rate":
        plant, rating = info.split(" - ")
        rating = int(rating)
        if plant in catalogue.keys():
            catalogue[plant].append(rating)  # key: [ 0 - > rarity, 1+ ratings]
        else:
            print("error")
    elif action == "Update":
        plant, new_rarity = info.split(" - ")
        if plant in catalogue.keys():
            new_rarity = int(new_rarity)
            org_val = catalogue[plant]
            org_val.pop(0)
            org_val.insert(0, new_rarity)
            catalogue[plant] = org_val
        else:
            print("error")
    elif action == "Reset":
        plant = info
        if plant in catalogue.keys():
            org_val = catalogue[plant]
            for i in range(1, len(catalogue[plant])):
                catalogue[plant].pop()
        else:
            print("error")
    command = input()
print("Plants for the exhibition:")
for plant in catalogue.keys():
    if len(catalogue[plant]) < 2:
        avg_rat_cur_plant = 0
    else:
        for i in range(1, len(catalogue[plant])):
            avg_rat_cur_plant += catalogue[plant][i]
        length = len(catalogue[plant])
        avg_rat_cur_plant /= (length - 1)
    print(f"- {plant}; Rarity: {catalogue[plant][0]}; Rating: {avg_rat_cur_plant:.2f}")
    avg_rat_cur_plant = 0
