lost_fight_count = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())
total_expenses = 0
shield_broken_counter = 0

for fight_counter in range(1, lost_fight_count + 1):
    if fight_counter % 2 == 0:
        total_expenses += price_helmet
    if fight_counter % 3 == 0:
        total_expenses += price_sword
    if fight_counter % 2 == 0 and fight_counter % 3 == 0:
        total_expenses += price_shield
        shield_broken_counter += 1
    if shield_broken_counter == 2:
        total_expenses += price_armor
        shield_broken_counter = 0

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
