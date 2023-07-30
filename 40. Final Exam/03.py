zoo_db = {}
cmd = input()
while cmd != "EndDay":
    action, info = cmd.split(": ")
    if action == "Add":
        animal_name, food_needed, area = info.split("-")
        food_needed = int(food_needed)
        if area in zoo_db:
            if animal_name in zoo_db[area]:
                zoo_db[area][animal_name] += food_needed
            else:
                zoo_db[area][animal_name] = food_needed
        else:
            zoo_db[area] = {animal_name: food_needed}

    elif action == "Feed":
        animal_name, food_fed = info.split("-")
        food_fed = int(food_fed)
        for area in zoo_db:
            if animal_name in zoo_db[area]:
                zoo_db[area][animal_name] -= food_fed
                if zoo_db[area][animal_name] <= 0:
                    print(f"{animal_name} was successfully fed")
                    zoo_db[area].pop(animal_name)
    cmd = input()
print("Animals:")
for area in zoo_db:
    for animal in zoo_db[area]:
        print(f" {animal} -> {zoo_db[area][animal]}g")
print("Areas with hungry animals:")
for area in zoo_db:
    if zoo_db[area]:
        print(f" {area}: {len(zoo_db[area])}")

# Add: Adam-4500-ByTheCreek
# Add: Maya-7600-WaterfallArea
# Add: Maya-1230-WaterfallArea
# Feed: Jamie-2000
# EndDay

# Add: Jamie-600-WaterfallArea
# Add: Maya-6570-WaterfallArea
# Add: Adam-4500-ByTheCreek
# Add: Bobbie-6570-WaterfallArea
# Feed: Jamie-2000
# Feed: Adam-2000
# Feed: Adam-2500
# EndDay