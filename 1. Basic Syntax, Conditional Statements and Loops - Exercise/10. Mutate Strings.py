first_word = input()
second_word = input()
for char in range(0, len(first_word)):
    if first_word[char] != second_word[char]:
        first_word = second_word[0:char + 1] + first_word[char + 1:]
        print(first_word)
