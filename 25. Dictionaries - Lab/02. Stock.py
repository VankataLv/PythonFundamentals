stock = {}
initial_data = input().split(" ")
for i in range(0, len(initial_data), 2):
    key = initial_data[i]
    amount = initial_data[i + 1]
    stock[key] = amount

inquiries = input().split(" ")
for inquiry in inquiries:
    if inquiry in stock:
        print(f"We have {stock[inquiry]} of {inquiry} left")
    else:
        print(f"Sorry, we don't have {inquiry}")

# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes

# eggs 5 bread 10
# bread eggs