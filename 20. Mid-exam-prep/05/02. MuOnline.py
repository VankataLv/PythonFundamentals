health = 100
coins = 0
rooms = input().split("|")
room_number = 0

for stuff in rooms:
    room_number += 1
    command, number = stuff.split(" ")
    number = int(number)
    if command == "potion":
        if health + number > 100:
            number -= health + number - 100
        print(f"You healed for {number} hp.")
        health += number
        print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        coins += number
    else:                                   # monster case
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            quit()

print("You've made it!")
print(f"Bitcoins: {coins}")
print(f"Health: {health}")
