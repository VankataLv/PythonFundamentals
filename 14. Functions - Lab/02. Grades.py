grade_digit = float(input())


def grade_converter(grade: float):
    if 2 <= grade <= 2.99:
        print("Fail")
    elif 3 <= grade <= 3.49:
        print("Poor")
    elif 3.5 <= grade <= 4.49:
        print("Good")
    elif 4.5 <= grade <= 5.49:
        print("Very Good")
    elif 5.5 <= grade <= 6.00:
        print("Excellent")


grade_converter(grade_digit)
