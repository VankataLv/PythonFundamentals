targets = list(map(int, input().split(" ")))
shot_targets = 0
command = input()
new_list_tgts = []
while command != "End":
    command = int(command)
    if command > len(targets) - 1:
        command = input()
        continue
    else:
        target_value = targets[command]
        for x in targets:
            if x == -1:
                new_list_tgts.append(x)
                continue
            if x > target_value:
                x -= target_value
            else:
                x += target_value
            new_list_tgts.append(x)
        targets = new_list_tgts
        new_list_tgts = []
        targets[command] = -1
    command = input()
print(f"Shot targets: {targets.count(-1)} -> ", end="")
for el in targets:
    print(el, end=" ")
