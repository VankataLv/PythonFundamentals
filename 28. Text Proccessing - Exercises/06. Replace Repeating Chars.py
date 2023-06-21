repeated_text = input()
clear_text = ""
for i in range(len(repeated_text) - 1):
    if repeated_text[i] == repeated_text[i + 1]:
        continue
    else:
        clear_text += repeated_text[i]
clear_text += repeated_text[-1]
print(clear_text)