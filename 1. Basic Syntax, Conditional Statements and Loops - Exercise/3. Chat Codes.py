n = int(input())

for i in range(1, n + 1):
    user_input = int(input())
    if user_input == 88:
        print("Hello")
    elif user_input == 86:
        print("How are you?")
    elif user_input < 88 and user_input != 86:
        print("GREAT!")
    elif user_input > 88:
        print("Bye.")
