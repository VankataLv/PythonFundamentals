pirate = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())
command = input()
while command != "Retire":
    token = command.split(" ")
    if token[0] == "Fire":
        index, damage = int(token[1]), int(token[2])
        if index in range(0, len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                quit()
    elif token[0] == "Defend":
        start_index, end_index, damage = int(token[1]), int(token[2]), int(token[3])
        if start_index in range(0, len(pirate)) and end_index in range(0, len(pirate)):
            for damaged_index in range(start_index, end_index + 1):
                pirate[damaged_index] -= damage
                if pirate[damaged_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    quit()
    elif token[0] == "Repair":
        index, health = int(token[1]), int(token[2])
        if index in range(0, len(pirate)):
            pirate[index] += health
            if pirate[index] > max_health:
                pirate[index] = max_health
    elif token[0] == "Status":
        counter = 0
        for section in pirate:
            if section < 0.2 * max_health:
                counter += 1
        print(f"{counter} sections need repair.")
    token.clear()
    command = input()
print(f"Pirate ship status: {sum(pirate)}")
print(f"Warship status: {sum(warship)}")
