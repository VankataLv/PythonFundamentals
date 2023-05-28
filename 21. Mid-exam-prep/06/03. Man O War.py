pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_section_health = int(input())
command = input()
while command != "Retire":
    if command[0:4] == "Fire":
        action, index, damage = command.split(" ")
        index = int(index)
        damage = int(damage)
        if index in range(-len(warship), len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                quit()
        else:
            command = input()
            continue
    elif command[0:6] == "Defend":
        action, start_index, end_index, damage = command.split(" ")
        start_index = int(start_index)
        end_index = int(end_index)
        damage = int(damage)
        if start_index in range(-len(pirate_ship), len(pirate_ship)) and end_index in range(-len(pirate_ship), len(pirate_ship)):     # check if range is valid
            for section in range(start_index, end_index + 1):
                pirate_ship[section] -= damage
                if pirate_ship[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    quit()
        else:
            command = input()
            continue
    elif command[0:6] == "Repair":
        action, index, health = command.split(" ")
        index = int(index)
        health = int(health)
        if index in range(-len(pirate_ship), len(pirate_ship)):
            pirate_ship[index] += health
            if pirate_ship[index] > max_section_health:
                pirate_ship[index] = max_section_health
    elif command[0:7] == "Status":
        repair_needed = [section for section in pirate_ship if section < max_section_health * 0.2]
        print(f"{len(repair_needed)} sections need repair.")
    command = input()

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")
