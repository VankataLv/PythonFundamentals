my_list_letters = ["a", "m", "k", "c"]
numbers_my_list = [1, 2, 3, 6, 8, 99, 5, 2, 2]

# my_list_letters.sort(reverse=True)
# my_list_letters.sort()
# print(my_list_letters)

# numbers_my_list.sort()
# print(numbers_my_list)

# ---- THis how u save the "popped" index from a list
# char = numbers_my_list.pop()
# print(numbers_my_list)
# print(char)

# ---- Enumerate -----
# indexes_list = []
# for index, element in enumerate(numbers_my_list):
#     if element == 2:
#         indexes_list.append(index)
# print(indexes_list)

# ----- Reversing(1) and Reversing printing-slicing(2) of lists- -----
# numbers_my_list.reverse()
# print(numbers_my_list)

# print(numbers_my_list[::-1])

# ---- copy vs = ---- (reference!)
# if using = -> list1 = list2 everything changes for both lists
# elif using .copy -> list2 = list1.copy() you have two independent lists


# Return double of n
# def addition(n):
#     return n + n
#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))