vowels = ["a", "o", "u", "e", "i"]
text = input()
no_vowel_text = [char for char in text if char.lower() not in vowels]
new_string = "".join(no_vowel_text)
print(new_string)