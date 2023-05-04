lst_numbers_random = input().split(" ")
numbers_remove = int(input())

lst_numbers_integer = [int(i) for i in lst_numbers_random]  # converting all values to int IOT sort them
for number_to_remove in range(numbers_remove):
    lst_numbers_integer.remove(min(lst_numbers_integer))    # remove the smallest number, number_remove times

for index in range(0, len(lst_numbers_integer) - 1):
    print(f"{lst_numbers_integer[index]}, ", end="")
print(lst_numbers_integer[-1])

# print(", ".join(str(x) for x in lst_numbers_integer))    # shorter solution

