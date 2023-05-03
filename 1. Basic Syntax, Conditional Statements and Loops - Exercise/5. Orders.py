number_orders = int(input())
total_cost = 0

for order_number in range(1, number_orders + 1):

    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        current_order = price_capsule * capsules_per_day * days
        print(f"The price for the coffee is: ${current_order:.2f}")
        total_cost += current_order
        current_order = 0

    else:
        continue

print(f"Total: ${total_cost:.2f}")
