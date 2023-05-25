shopping_list = list(input().split("!"))
command = input().strip()
while command != "Go Shopping!":
    if command[0:7] == "Correct":
        action, old_item, new_item = command.split(" ")
        if old_item in shopping_list:
            index_old_item = shopping_list.index(old_item)
            shopping_list[index_old_item] = new_item
        else:
            command = input().strip()
            continue
    else:
        action, item = command.split(" ")
        if action == "Urgent":
            if item in shopping_list:
                command = input().strip()
                continue
            else:
                shopping_list.insert(0, item)
        if action == "Unnecessary":
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                command = input().strip()
                continue
        if action == "Rearrange":
            if item in shopping_list:
                shopping_list.remove(item)
                shopping_list.append(item)
            else:
                command = input().strip()
                continue
print(", ".join(shopping_list))
