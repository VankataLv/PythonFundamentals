budget = int(input())
money_spent = 0
user_command = 0
while user_command != "End":
    current_product_price = int(user_command)
    money_spent += current_product_price
    if money_spent > budget:
        print("You went in overdraft!")
        quit()
    user_command = input()

print("You bought everything needed.")
