coins = input().split(", ")
beggars = int(input())
beggar_earnings = []
current_beggar_earnings = 0

if len(coins) > beggars:
    for beggar in range(beggars):
        for i in range(0 + beggar, len(coins), len(coins) // 2):
            current_beggar_earnings += int(coins[i])
        beggar_earnings.insert(beggar, current_beggar_earnings)
        current_beggar_earnings = 0


print(beggar_earnings)
