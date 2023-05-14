from math import factorial
first_num = int(input())
second_num = int(input())


def fact_divisor(a: int, b: int):
    fact_a = factorial(a)
    fact_b = factorial(b)

    print(f"{fact_a/fact_b:.2f}")


fact_divisor(first_num, second_num)