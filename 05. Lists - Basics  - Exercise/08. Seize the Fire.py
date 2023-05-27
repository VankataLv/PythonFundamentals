admin_list = input().split("#")
amount_water = int(input())
effort = 0
total_fire_extinguished = 0
cells_extinguished = list()
for iteration in range(len(admin_list)):                            # how many times will we execute
    current_value_admin_list = admin_list[iteration]                # get the values for the current iteration
    type_fire, value_cell = current_value_admin_list.split(" = ")   # split the values in variables for current iteration
    value_cell = int(value_cell)                                    # after split convert value_cell to int IOT compare it for validity
                                                                    # code can be simplified with any([....])
    if type_fire == "High":                                         # check if value_cell is valid
        if value_cell not in range(81, 126):                        # 81 , 126 because range ending is not inclusive (81, (125 + 1))
            continue                                                # invalid cell value
        else:
            if amount_water >= value_cell:                          # Check do we have enough water
                amount_water -= value_cell
                effort += 0.25 * value_cell
                total_fire_extinguished += value_cell
                cells_extinguished.append(value_cell)               # store the extinguished cell

    elif type_fire == "Medium":
        if value_cell not in range(51, 81):
            continue
        else:
            if amount_water >= value_cell:  # Check do we have enough water
                amount_water -= value_cell
                effort += 0.25 * value_cell
                total_fire_extinguished += value_cell
                cells_extinguished.append(value_cell)  # store the extinguished cell

    elif type_fire == "Low":
        if value_cell not in range(1, 51):
            continue
        else:
            if amount_water >= value_cell:  # Check do we have enough water
                amount_water -= value_cell
                effort += 0.25 * value_cell
                total_fire_extinguished += value_cell
                cells_extinguished.append(value_cell)  # store the extinguished cell

print("Cells:")
for value_extinguished_cell in cells_extinguished:
    print(f' - {value_extinguished_cell}')
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire_extinguished}")

# inputs -------------

# High = 89#Low = 28#Medium = 77#Low = 23
# 1250
