first_sen = input().split(", ")
second_sen = input().split(", ")

substrings = [substring for substring in first_sen for element_second in second_sen if substring in element_second]
substrings = list(dict.fromkeys(substrings))
print(substrings)

