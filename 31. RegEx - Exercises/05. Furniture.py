import re
total_cost = 0
data = []
command = input()
pattern = r">>(?P<el>[A-Z]+[a-z]*)<<(?P<price>\d+\.?\d+)!(?P<qty>\d+)"
while command != "Purchase":
    data = re.finditer(pattern, command)
    command = input()
print("Bought furniture:")
for el in data:
    cur_piece = el.groupdict()
    print(f"{cur_piece['el']}")
    cur_price = float(cur_piece['price'])
    cur_qty = int(cur_piece['qty'])
    total_cost += cur_price * cur_qty
print(f"Total money spend: {total_cost:.2f}")
