num_list = list(map(int, input().split(" ")))
even_num = list()


def even_num_filter(numbers: list):
    for number in numbers:
        if number % 2 == 0:
            even_num.append(number)
    return even_num


print(even_num_filter(num_list))
