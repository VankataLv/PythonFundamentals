def char_range(a: str, b: str):
    lower_limit = min(ord(a), ord(b))
    higher_limit = max(ord(a), ord(b))
    symbols = ""

    for char in range(lower_limit + 1, higher_limit):
        symbols = symbols + chr(char) + " "

    return symbols


first_character = input()
second_character = input()
print(char_range(first_character, second_character))
