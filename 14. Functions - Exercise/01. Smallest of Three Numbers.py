first_num = int(input())
second_num = int(input())
third_num = int(input())


def find_smallest(a, b, c):
    return min(a, b, c)


result = find_smallest(first_num, second_num, third_num)
print(result)
