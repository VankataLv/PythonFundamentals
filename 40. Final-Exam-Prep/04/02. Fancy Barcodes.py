import re

lst_valid_barcodes = []
n = int(input())
product_group = ""
pattern = r"@#+([A-Z]+[A-Za-z\d]{4,}[A-Z])+@#+"
for iteration in range(n):
    txt = input()
    valid_barcode = re.findall(pattern, txt)
    if not valid_barcode:
        print("Invalid barcode")
        continue
    for item in valid_barcode:
        for char in item:
            if char.isdigit():
                product_group += char
        if len(product_group) == 0:
            product_group = "00"
    print(f"Product group: {product_group}")
    product_group = ""


