energy_left = int(input())
wins = 0
command = input()
while energy_left > 0 and command != "End of battle":
    distance = int(command)
    if energy_left >= distance:
        energy_left -= distance
        wins += 1
        if wins % 3 == 0:
            energy_left += wins
    else:
        break
    command = input()

if command == "End of battle":
    print(f"Won battles: {wins}. Energy left: {energy_left}")
else:
    print(f"Not enough energy! Game ends with {wins} won battles and {energy_left} energy")
