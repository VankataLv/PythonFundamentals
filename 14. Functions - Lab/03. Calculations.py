operator = input()
first_num = int(input())
second_num = int(input())


def integer_calculator(action: str, a: int, b: int):
    if action == "multiply":
        return a * b
    elif action == "divide":
        return a // b
    elif action == "add":
        return a + b
    elif action == "subtract":
        return a - b


print(integer_calculator(operator, first_num, second_num))
