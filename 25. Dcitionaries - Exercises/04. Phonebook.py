phonebook = {}
while True:
    info = input()
    if "-" not in info:
        break
    else:
        key, num = info.split("-")  # info will be a ["name", "########"]
        phonebook[key] = num
for search in range(int(info)):
    name_searched = input()
    if name_searched in phonebook.keys():
        print(f"{name_searched} -> {phonebook[name_searched]}")
    else:
        print(f"Contact {name_searched} does not exist.")
