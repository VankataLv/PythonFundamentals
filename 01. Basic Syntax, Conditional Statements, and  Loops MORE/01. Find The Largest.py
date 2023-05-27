user_input = int(input())
highest_value = list(str(user_input))
highest_value.sort(reverse=True)
for i in highest_value:
    print(i, end="")
