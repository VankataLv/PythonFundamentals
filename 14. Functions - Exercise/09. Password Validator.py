def validator(pswrd):
    digit_counter = 0
    validity = True
    if not 6 <= len(pswrd) <= 10:
        print("Password must be between 6 and 10 characters")
        validity = False
    for char in pswrd:
        if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            pass
        else:
            print("Password must consist only of letters and digits")
            validity = False
            break
    for char in pswrd:
        if 48 <= ord(char) <= 57:
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        validity = False

    return validity


password_given = input()
if validator(password_given):
    print("Password is valid")
