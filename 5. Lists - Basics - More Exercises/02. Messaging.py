seq_numbers = input().split(" ")
message = input()
sum_numbers = ""
sum_to_convert = 0
for char in range(len(seq_numbers)):   # Take the groups of numbers
    sum_numbers = seq_numbers[char]
    for digit in range(len(sum_numbers)):
        sum_to_convert += int(sum_numbers[digit])   # Sum all the digits in the group
    while sum_to_convert > len(message):            # In case the sum is longer than the length of the key
        sum_to_convert -= len(message)
    print(message[sum_to_convert], end="")
    message = message[:sum_to_convert] + message[sum_to_convert + 1:]   # Slicing the string to take the used char
    sum_to_convert = 0
