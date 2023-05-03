n = int(input())
special_num = False
sum_of_digits = 0
for number in range(1, n+1):
    for digit in range(0, len(str(number))):
        sliced_number = str(number)
        sum_of_digits += int(sliced_number[digit])
    if sum_of_digits == 11 or sum_of_digits == 5 or sum_of_digits == 7:
        special_num = True
    if special_num:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
    sum_of_digits = 0
    special_num = False
