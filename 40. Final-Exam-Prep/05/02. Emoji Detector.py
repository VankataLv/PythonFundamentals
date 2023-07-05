import re
cool_t = 1
txt = input()
for char in txt:
    if char.isdigit():
        char = int(char)
        cool_t *= char
print(f"Cool threshold: {cool_t}")

pattern = r"(::|\*\*)([A-Z]+[a-z]{2,})(\1)"
matches = re.findall(pattern, txt)
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for emoji in matches:
    cur_emoji = emoji[1]
    cur_sum = 0
    for char in cur_emoji:
        cur_sum += ord(char)
    if cur_sum >= cool_t:
        emoji_to_print = emoji[0] + emoji[1] + emoji[2]
        print(f"{emoji_to_print}")
