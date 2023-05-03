qty_decorations = int(input())
days_left = int(input())
total_cost = 0
total_spirit = 0
same_day_bonus = False
for day_counter in range(1, days_left + 1):
    same_day_bonus = False
    if day_counter % 11 == 0:
        qty_decorations += 2
    if day_counter % 2 == 0:
        total_cost += 2 * qty_decorations
        total_spirit += 5
    if day_counter % 3 == 0:
        total_cost += 8 * qty_decorations
        total_spirit += 13
        same_day_bonus = True
    if day_counter % 5 == 0:
        total_cost += 15 * qty_decorations
        total_spirit += 17
        if same_day_bonus:
            total_spirit += 30
    if day_counter % 10 == 0:
        total_cost += 23
        total_spirit -= 20

if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
