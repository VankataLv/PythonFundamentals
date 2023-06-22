text = input()
new_text = ""
strenth = 0
for i in range(len(text)):
    if strenth > 0 and text[i] != ">":
        strenth -= 1
    elif text[i] == ">":
        new_text += text[i]
        strenth += int(text[i+1])
    else:
        new_text += text[i]
print(new_text)