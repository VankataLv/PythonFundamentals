text = input().split(" ")
elements_even_len = [element for element in text if len(element) % 2 == 0]
[print(element) for element in elements_even_len]