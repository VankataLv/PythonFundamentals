seq = input().split(" ")
for el in seq:
    n = len(el)
    print(f"".join(el)*n, end="")
