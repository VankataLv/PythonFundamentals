banned_words = input().split(", ")
text = input()
for word in banned_words:
    while word in text:
        text = text.replace(word, "*" * len(word))
print(text)

# Linux, Windows
# It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client
