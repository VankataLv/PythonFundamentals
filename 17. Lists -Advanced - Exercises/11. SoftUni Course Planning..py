cur = [el for el in input().split(", ")]
command = input()
ex_swap_1 = False
ex_swap_2 = False
while command != "course start":
    command = command.split(":")   # 0 -> action; 1 -> lesson Title; 2 if it exists -> index or swapped lesson Tile
    if command[0] == "Add":
        if command[1] not in cur:
            cur.append(command[1])
    elif command[0] == "Insert":
        if command[1] not in cur:
            cur.insert(int(command[2]), command[1])
    elif command[0] == "Remove":
        if command[1] in cur:
            cur.remove(command[1])
        if f"{command[1]}-Exercise" in cur:
            cur.remove(f"{command[1]}-Exercise")
    elif command[0] == "Swap":
        if command[1] in cur and command[2] in cur:
            first_el = command[1]
            i_1 = cur.index(first_el)
            if ":" in command[i_1 + 1]:
                ex_swap_1 = True
            second_el = command[2]
            i_2 = cur.index(second_el)
            if ":" in command[i_1 + 1]:
                ex_swap_2 = True
            cur[i_1], cur[i_2] = second_el, first_el
            if ex_swap_1:
                ex_to_swap = cur[i_1 + 1]
                cur.insert(i_2 + 1, ex_to_swap)
                cur.pop(i_1 + 1)
                ex_swap_1 = False
            if ex_swap_2:
                ex_to_swap = cur[i_2 + 1]
                cur.insert(i_1 + 1, ex_to_swap)
                cur.pop(i_2 + 1)
                ex_swap_2 = False
    elif command[0] == "Exercise":
        if command[1] not in cur:
            cur.append(command[1])
            cur.append(f"{command[1]}-Exercise")
            command = input()
            continue
        if command[1] == command[-1]:
            cur.append(f"{command[1]}-Exercise")
            command = input()
            continue
        i_lesson = cur.index(command[1])
        next_lesson = cur[i_lesson + 1]
        if ":" not in next_lesson:
            cur.insert(i_lesson + 1, f"{command[1]}-Exercise")
    command = input()
for index, el in enumerate(cur):
    print(f"{index + 1}.{el}")

# Data Types, Objects, Lists
# Add:Databases
# Insert:Arrays:0
# Remove:Lists
# course start

# Arrays, Lists, Methods
# Swap:Arrays:Methods
# Exercise:Databases
# Swap:Lists:Databases
# Insert:Arrays:0
# course start