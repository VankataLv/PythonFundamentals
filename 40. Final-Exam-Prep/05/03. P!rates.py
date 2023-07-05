cities = {}
command = input()
while command != "Sail":
    city, pop, gold = command.split("||")
    if city in cities.keys():
        cities[city][0] += int(pop)
        cities[city][1] += int(gold)
    else:
        cities[city] = [int(pop), int(gold)]  # city: [0->pop, 1->gold]
    command = input()
event = input()
while event != "End":
    action, details = event.split("=>", 1)
    if action == "Plunder":
        town, people, gold = details.split("=>")
        people, gold = int(people), int(gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town][0] -= people
        cities[town][1] -= gold
        if cities[town][0] == 0 or cities[town][1] == 0:
            print(f"{town} has been wiped off the map!")
            cities.pop(town)
    elif action == "Prosper":
        town, gold = details.split("=>")
        gold = int(gold)
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    event = input()
if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key in cities.keys():
        print(f"{key} -> Population: {cities[key][0]} citizens, Gold: {cities[key][1]} kg")
