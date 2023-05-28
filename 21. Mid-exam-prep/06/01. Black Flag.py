days = int(input())
plunder_day = int(input())
goal_plunder = float(input())
current_plunder = 0

for day in range(1, days + 1):
    current_plunder += plunder_day
    if day % 3 == 0:
        current_plunder += plunder_day * 0.5
    if day % 5 == 0:
        current_plunder *= 0.7
if current_plunder >= goal_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    percentage = (current_plunder / goal_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
