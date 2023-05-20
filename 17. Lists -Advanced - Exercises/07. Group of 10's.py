seq_nums = input().split(", ")
seq_nums = [int(x) for x in seq_nums]
current_list = []
max_group = max(seq_nums) + 10
for current_group in range(10, max_group, 10):
    for el in seq_nums:
        if current_group - 10 < el <= current_group:
            current_list.append(el)

    print(f"Group of {current_group}'s: {current_list}")
    current_list = []
