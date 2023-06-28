import re
text = input()
pattern = r"(\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b)"
valid_phone_nums = re.findall(pattern, text)
print(", ".join(valid_phone_nums))

# +359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222