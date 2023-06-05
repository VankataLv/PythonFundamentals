commands = input()
stock = {}
while commands != "statistics":
    product, value = commands.split(": ")
    if product not in stock:
        stock[product] = int(value)
    else:
        stock[product] += value
    commands = input()

print("Products in stock:")
for key in stock:
    print(f"- {key}: {stock[key]}")

print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")

# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics
