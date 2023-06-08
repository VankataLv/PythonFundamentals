from math import sqrt
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

# first line is (a1, b1) (a2, b2) -> forms triangle with sides a, b, c-hypo
# second line is (d1, e1) (d2, e2) -> forms triangle with sides d, e, f-hypo
def pythagorian_theorem_hypo(a1, b1, a2, b2, d1, e1, d2, e2):
    side_a = abs(a1) + abs(a2)
    side_b = abs(b1) + abs(b2)
    hypo_c = sqrt((side_a ** 2) + (side_b ** 2))
    side_d = abs(d1) + abs(d2)
    side_e = abs(e1) + abs(e2)
    hypo_f = sqrt((side_d ** 2) + (side_e ** 2))
    if hypo_c >= hypo_f:
        side_g = abs(a1)
        side_h = abs(b1)
        hypo_i = sqrt((side_g ** 2) + (side_h ** 2))
        side_j = abs(a2)
        side_k = abs(b2)
        hypo_l = sqrt((side_j ** 2) + (side_k ** 2))
        a1 = int(a1)
        b1 = int(b1)
        a2 = int(a2)
        b2 = int(b2)
        if hypo_i < hypo_l:
            print(f"({int(a1)}, {b1})({a2}, {b2})")
        else:
            print(f"({int(a2)}, {b2})({a1}, {b1})")
    else:
        side_g = abs(d1)
        side_h = abs(e1)
        hypo_i = sqrt((side_g ** 2) + (side_h ** 2))
        side_j = abs(d2)
        side_k = abs(e2)
        hypo_l = sqrt((side_j ** 2) + (side_k ** 2))
        d1 = int(d1)
        e1 = int(e1)
        d2 = int(d2)
        e2 = int(e2)
        if hypo_i < hypo_l:
            print(f"({d1}, {e1})({d2}, {e2})")
        else:
            print(f"({d2}, {e2})({d1}, {e1})")

pythagorian_theorem_hypo(x1, y1, x2, y2, x3, y3, x4, y4)
