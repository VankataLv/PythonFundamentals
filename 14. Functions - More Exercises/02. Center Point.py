from math import sqrt, floor
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def pythagorian_theorem_hypo(a1, b1, a2, b2):
    hypotenuse_1 = sqrt((abs(a1) ** 2) + (abs(b1) ** 2))
    hypotenuse_2 = sqrt((abs(a2) ** 2) + (abs(b2) ** 2))

    a1 = floor(int(a1))
    b1 = floor(int(b1))
    a2 = floor(int(a2))
    b2 = floor(int(b2))

    if hypotenuse_1 <= hypotenuse_2:
        print(f"({a1}, {b1})")
    else:
        print(f"({a2}, {b2})")


pythagorian_theorem_hypo(x1, y1, x2, y2)
