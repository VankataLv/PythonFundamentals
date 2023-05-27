group_size = int(input())
days = int(input())
coins_left = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    coins_left += 50 - (2 * group_size)
    if day % 3 == 0:
        coins_left -= 3 * group_size
    if day % 5 == 0:
        coins_left += 20 * group_size
        if day % 3 == 0:
            coins_left -= 2 * group_size

print(f"{group_size} companions received {coins_left // group_size} coins each.")
