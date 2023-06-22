def calc(word: str) -> int:
    first_char = word[0]
    last_char = word[-1]
    letters = int(word[1:len(word) - 1])
    if first_char.isupper():
        first_char_dgt = ord(first_char) - 64
        letters /= first_char_dgt
    else:
        first_char_dgt = ord(first_char) - 96
        letters *= first_char_dgt
    if last_char.isupper():
        last_char_dgt = ord(last_char) - 64
        letters -= last_char_dgt
    else:
        last_char_dgt = ord(last_char) - 96
        letters += last_char_dgt
    return letters


text = input()
cur_word = ""
text += " "
total_sum = 0
for i in range(len(text)):
    if text[i] == " ":
        if len(cur_word) == 0:
            continue
        total_sum += calc(cur_word)
        cur_word = ""
    else:
        cur_word += text[i]
print(f"{total_sum:.2f}")
