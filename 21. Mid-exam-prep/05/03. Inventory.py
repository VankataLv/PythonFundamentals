journal = input().split(", ")
command = input()

while command != "Craft!":
    if command[0:13] == "Combine Items":
        action, items = command.split(" - ")
        old_item, new_item = items.split(":")
        if old_item in journal:
            index_old_item = journal.index(old_item)        # find the index of the old item
            index_new_item = index_old_item + 1
            journal.insert(index_new_item, new_item)
        else:
            command = input()
            continue
    else:
        action, item = command.split(" - ")
        if action == "Collect":
            if item in journal:
                command = input()
                continue
            else:
                journal.append(item)
        elif action == "Drop":
            if item in journal:
                journal.remove(item)
            else:
                command = input()
                continue
        elif action == "Renew":
            if item in journal:
                journal.remove(item)
                journal.append(item)
            else:
                command = input()
                continue
    command = input()
print(", ".join(journal))
