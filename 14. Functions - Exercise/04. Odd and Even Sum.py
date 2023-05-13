original_number = input()


def odd_and_even_sum(num_string: str):
    odd_sum = 0
    even_sum = 0
    for num in num_string:
        if int(num) % 2 == 1:
            odd_sum += int(num)
        elif int(num) % 2 == 0:
            even_sum += int(num)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(odd_and_even_sum(original_number))
