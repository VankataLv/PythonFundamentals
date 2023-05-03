number_lines = int(input())   # in an interval [1:20]
total_sum = 0

for line_count in range(number_lines):
    user_input = input()
    total_sum += ord(user_input)

print(f"The sum equals: {total_sum}")
