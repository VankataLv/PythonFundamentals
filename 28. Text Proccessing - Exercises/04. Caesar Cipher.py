original_text = input()
encrypted_text = ""
for char in original_text:
    encrypted_text += chr(ord(char) + 3)
print(encrypted_text)