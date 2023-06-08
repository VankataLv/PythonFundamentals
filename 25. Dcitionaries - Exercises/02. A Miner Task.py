command = input()
line_count = 0
storage = {}
res = ""
quantity = 0
while command != "stop":
    line_count += 1
    if line_count % 2 == 1:
        res = command
        if res in storage:
            command = input()
            continue
        else:
            storage[res] = 0
    else:
        quantity = int(command)
        storage[res] += quantity
    command = input()

for key, value in storage.items():
    print(f"{key} -> {value}")
