text = input()
symbols = []
rage_text = ""
cur_word = ""
two_digit_num = False
prv_char = ""
for char in text:
    if char.isdigit():
        if two_digit_num:
            rage_text += cur_word * (int(prv_char + char))
            cur_word = ""
            two_digit_num = False
            continue
        else:
            two_digit_num = True
            prv_char = char
    elif len(prv_char) > 0:
        rage_text += cur_word * int(prv_char)
        prv_char = ""
    else:
        symbols.append(char)
        cur_word += char.upper()
print(f"Unique symbols used: {len(set(symbols))}")
print(rage_text)
