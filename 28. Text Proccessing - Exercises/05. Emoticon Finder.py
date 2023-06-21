text = input()
emotis = []
for i in range(len(text)):
    if text[i] == ":":
        emoji = text[i] + text[i + 1]
        emotis.append(emoji)
for el in emotis:
    print(el)