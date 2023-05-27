seq_numbers = input().split(" ")
message = input()
hidden_text = list()
sum_numbers = ""
sum_to_convert = 0
for char in range(len(seq_numbers)):
    sum_numbers = seq_numbers[char]
    for digit in range(len(sum_numbers)):
        sum_to_convert += int(sum_numbers[digit])
    while sum_to_convert > len(message):
        sum_to_convert -= len(message)
    print(message[sum_to_convert], end="")
    message = message[:sum_to_convert] + message[sum_to_convert + 1]

# input________
# 9992 562 8933
# This is some message for you
