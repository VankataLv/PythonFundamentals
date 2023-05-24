numbers = list(map(int, input().split(" ")))
avg_numbers = sum(numbers) / len(numbers)
nums_higher_avg = [num for num in numbers if num > avg_numbers]
counter = 0
if len(nums_higher_avg) > 0:
    nums_higher_avg.sort(reverse=True)
    for i in range(len(nums_higher_avg)):
        if counter == 5:
            break
        print(f'{nums_higher_avg[i]} ', end="")
        counter += 1
else:
    print("No")
