number_lines = int(input())
current_water_level = 0
for counter in range(0, number_lines):
    litres_to_add = int(input())
    if current_water_level + litres_to_add > 255:
        print("Insufficient capacity!")
    else:
        current_water_level += litres_to_add
print(current_water_level)