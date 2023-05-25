target_range = list(map(int, input().split(" ")))
command = input()
while command != "End":
    sorted_command = command.split(" ")
    action = sorted_command[0]
    index = int(sorted_command[1])
    value = int(sorted_command[2])
    if action == "Shoot":
        if 0 <= index < len(target_range):
            target_range[index] -= value
            if target_range[index] <= 0:
                target_range.pop(index)
        else:
            continue
    elif action == "Add":
        pass
    elif action == "Strike":                        # value is the radius of the strike
        if index - value < 0 or index + value >= len(target_range):  # invalid strike
            print("Strike missed!")
            continue
        else:
            strike_indexes = []
            for lower_index in range(index - 1, index - value - 1, - 1):
                strike_indexes.append(lower_index)
            for higher_index in range(index, index + value + 1):  # including the strike center -> index variable
                strike_indexes.append(higher_index)
            strike_indexes.sort(reverse=True)                      # reverse the list so that pop starts from the highest index
            for strike_index in strike_indexes:
                target_range.pop(index)
    print(target_range)
    command = input()