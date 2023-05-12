def repeater(text_to_repeat: str, times_to_repeat: int):
    return text_to_repeat * times_to_repeat


original_text = input()
counter = int(input())
repeated_text = repeater(original_text, counter)
print(repeated_text)
