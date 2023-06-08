orders = {}
command = input()
while command != "buy":
    name, price, quantity = command.split(" ")   # {name} {price} {quantity}"
    price = float(price)
    quantity = int(quantity)
    if name not in orders.keys():
        orders[name] = [price, quantity]  # [0->price, 1->qty]
    else:
        orders[name][0] = price
        orders[name][1] += quantity
    command = input()
for key, value in orders.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
