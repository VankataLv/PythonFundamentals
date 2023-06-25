import re
phone_nums = input()
pattern = r"(\+359)( )2( )\d{3}( )\d{4}\b|(\+359)(-)2(-)\d{3}(-)\d{4}\b"
valid_nums = re.finditer(pattern, phone_nums)
result = [num.group() for num in valid_nums]
print(", ".join(result))

#+359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222