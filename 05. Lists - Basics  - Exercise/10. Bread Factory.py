energy = 100
coins = 100
word_day_events = input().split("|")

for current_event in word_day_events:
    event_or_ingredient, number = current_event.split("-")
    number = int(number)
    if event_or_ingredient == "rest":
        if energy + number <= 100:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {(100 - energy)} energy.")
            print(f"Current energy: {100}.")
    elif event_or_ingredient == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:                                                   # ingredient case
        if coins >= number:
            coins -= number
            print(f"You bought {event_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            quit()

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
