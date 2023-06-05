data_keys = input().split(" ")
dct ={}

for el in data_keys:
    el = el.lower()
    if el in dct:
        dct[el] += 1
    else:
        dct[el] = 1
for key in dct:
    if dct[key] % 2 == 1:
        print(key, end=" ")
