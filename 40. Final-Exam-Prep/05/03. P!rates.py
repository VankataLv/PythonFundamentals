targets = {}
cmd = input()
while cmd != "Sail":
    city, pop, gold = cmd.split("||")
    pop, gold = int(pop), int(gold)
    if city in targets:
        targets[city]['pop'] += pop
        targets[city]['gold'] += gold
    else:
        targets[city] = {'pop': pop,
                         'gold': gold
                         }
    cmd = input()
cmd = input()
while cmd != "End":
    action, *info = cmd.split("=>")
    if action == "Plunder":
        city = info[0]
        pop_kia = int(info[1])
        gold_stolen = int(info[2])
        print(f"{city} plundered! {gold_stolen} gold stolen, {pop_kia} citizens killed.")
        targets[city]['pop'] -= pop_kia
        targets[city]['gold'] -= gold_stolen
        if targets[city]['pop'] <= 0 or targets[city]['gold'] <= 0:
            print(f"{city} has been wiped off the map!")
            targets.pop(city)
    elif action == "Prosper":
        city = info[0]
        gold_earned = int(info[1])
        if gold_earned < 0:
            print("Gold added cannot be a negative number!")
        else:
            targets[city]['gold'] += gold_earned
            print(f"{gold_earned} gold added to the city treasury. {city} now has {targets[city]['gold']} gold.")
    cmd = input()
if targets:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for city in targets:
        print(f"{city} -> Population: {targets[city]['pop']} citizens, Gold: {targets[city]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
