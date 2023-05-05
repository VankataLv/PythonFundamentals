coins = input().split(", ")
beggars = int(input())
beggar_earnings = []
current_beggar_earnings = 0

if len(coins) > beggars:
    for beggar in range(beggars):
        for i in range(0 + beggar, len(coins), beggars):
            current_beggar_earnings += int(coins[i])
        beggar_earnings.insert(beggar, current_beggar_earnings)
        current_beggar_earnings = 0
    print(beggar_earnings)

elif len(coins) == beggars:
    print([int(coin) for coin in coins])

elif len(coins) < beggars:
    for insufficient_coins in range(beggars - len(coins)):
        coins.append(str(0))
        print([int(coin) for coin in coins])
