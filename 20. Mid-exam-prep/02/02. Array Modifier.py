nums = list(map(int, input().split(" ")))
command = input()

while command != "end":
    if command == "decrease":
        nums = [num - 1 for num in nums]
    else:
        action, first_index, second_index = command.split(" ")
        first_index, second_index = int(first_index), int(second_index)
        if action == "swap":
            nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        if action == "multiply":
            nums[first_index] = nums[first_index] * nums[second_index]
    command = input()
result = [str(x) for x in nums]
print(", ".join(result))
