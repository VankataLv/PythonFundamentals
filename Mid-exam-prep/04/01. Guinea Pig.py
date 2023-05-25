qty_food = float(input()) * 1000
qty_hay = float(input()) * 1000
qty_cover = float(input()) * 1000
weight = float(input()) * 1000
for day in range(1, 31):
    qty_food -= 300
    if day % 2 == 0:
        qty_hay -= qty_food * 0.05
    if day % 3 == 0:
        qty_cover -= weight * (1 / 3)
if qty_food >= 0 and qty_cover >= 0 and qty_hay >= 0:
    print(
        f'Everything is fine! Puppy is happy! Food: {qty_food / 1000:.2f}, Hay: {qty_hay / 1000:.2f}, Cover: {qty_cover / 1000:.2f}.')
else:
    print("Merry must go to the pet store!")
