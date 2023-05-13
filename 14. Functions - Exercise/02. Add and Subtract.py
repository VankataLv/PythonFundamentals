first_num = int(input())
second_num = int(input())
third_num = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_subtract(a, b, c):
    sum_integers = sum_numbers(a, b)
    difference = subtract(sum_integers, c)
    print(difference)

add_subtract(first_num, second_num, third_num)
