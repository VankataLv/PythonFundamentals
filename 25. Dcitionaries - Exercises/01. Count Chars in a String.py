data = input().replace(" ", "")
count = {}
for char in data:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for el in count:
    print(f"{el} -> {count[el]}")
