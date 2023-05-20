total_electrons_left = int(input())
electrons_in_shells = []
free_electrons_positions = 0
current_layer = 1
while total_electrons_left > 0:
    free_electrons_positions = 2 * (current_layer ** 2)
    if total_electrons_left >= free_electrons_positions:
        electrons_in_shells.append(free_electrons_positions)
        total_electrons_left -= free_electrons_positions
        current_layer += 1
    else:
        electrons_in_shells.append(total_electrons_left)
        break

print(electrons_in_shells)
