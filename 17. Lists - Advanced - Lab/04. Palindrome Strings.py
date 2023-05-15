words = input().split(" ")
palin = input()

palindromes = [cur_el for cur_el in words if cur_el == cur_el[::-1]]
print(palindromes)
print(f"Found palindrome {words.count(palin)} times")
