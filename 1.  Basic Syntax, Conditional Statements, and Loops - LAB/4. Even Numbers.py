n = int(input())

for i in range(0, n):
    user_number = int(input())
    if user_number % 2 != 0:
        print(f"{user_number} is odd!")
        quit()
print("All numbers are even.")
