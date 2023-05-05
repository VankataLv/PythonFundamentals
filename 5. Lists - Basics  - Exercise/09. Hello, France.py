items = input().split("|")
budget = int(input())
price_new_items_bought = list()
prices_sold_items = list()

for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)
    if budget >= item_price:
        if any(["Clothes" in item_type and item_price <= 50,
                "Shoes" in item_type and item_price <= 35,
                "Accessories" in item_type and item_price <= 20.5]):
            price_new_items_bought.append(item_price)
            budget -= item_price
            prices_sold_items.append(item_price * 1.4)

for i in prices_sold_items:
    print(f"{i:.2f}", end=" ")

print(f'\nProfit: {sum(prices_sold_items) - sum(price_new_items_bought):.2f}')
if sum(prices_sold_items) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

# input ___________________________

# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120

# Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
# 90