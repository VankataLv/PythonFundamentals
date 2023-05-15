# nums = list(map(int, input().split(", ")))
nums = [int(element) for element in input(). split(", ")]

print([index for index in range(len(nums)) if nums[index] % 2 == 0])
