command = input()
total_price_no_tax = 0
discount = 1
taxes = 0
total_cost = 0
while command != "special" and command != "regular":
    price_item = float(command)
    if price_item <= 0:
        print("Invalid price!")
        command = input()
        continue
    else:
        total_price_no_tax += price_item
        command = input()
if total_price_no_tax > 0:
    taxes = total_price_no_tax * 0.2
    if command == "special":
        discount = 0.9
    total_cost = (total_price_no_tax + taxes) * discount
else:
    print("Invalid order!")
    quit()

print(f"Congratulations you've just bought a new computer!\n"
      f"Price without taxes: {total_price_no_tax:.2f}$\n"
      f"Taxes: {taxes:.2f}$\n"
      "-----------\n"
      f"Total price: {total_cost:.2f}$")

