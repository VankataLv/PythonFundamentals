data = input().split(" ")
bakery_stock = {}
for i in range(0, len(data), 2):
    bakery_stock[data[i]] = int(data[i + 1])

print(bakery_stock)
