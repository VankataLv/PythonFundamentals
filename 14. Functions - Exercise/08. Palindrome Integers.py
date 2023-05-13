possible_numbers = list(map(str, input().split(", ")))
for candidate in possible_numbers:
    reverse_candidate = candidate[::-1]
    if candidate == reverse_candidate:
        print("True")
    else:
        print("False")
