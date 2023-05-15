type_of_input = input()
number = input()


def calc(type_given: str, n):
    if type_given == "int":
        print(int(n) * 2)
    elif type_given == "real":
        print(f"{float(n)* 1.5:.2f}")
    elif type_given == "string":
        print("$" + n + "$")


calc(type_of_input, number)
