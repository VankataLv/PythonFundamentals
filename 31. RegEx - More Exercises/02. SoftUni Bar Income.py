import re

total_income = 0
pattern = r"%(?P<customer>[A-Z][a-z]+)%[^%\|\.\$]*<(?P<product>\w+)>[^%\|\.\$]*\|(?P<count>\d+)\|[^%\|\.\$]*?(?P<price>[0-9]+.?[0-9]+)\$"
cmd = input()
while cmd != "end of shift":
    match = re.match(pattern, cmd)
    if match:
        total_price = float(match.group("price")) * int(match.group("count"))
        customer = match.group('customer')
        product = match.group('product')
        print(f"{customer}: {product} - {total_price:.2f}")
        total_income += total_price
    cmd = input()
print(f"Total income: {total_income:.2f}")

