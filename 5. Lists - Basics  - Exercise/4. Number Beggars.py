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
    print([int(coin) for coin in coins])                                # converting all the values in the string to integers so when print no " "

elif len(coins) < beggars:
    for insufficient_coins in range(beggars - len(coins)):
        coins.append(str(0))                                            # add 0 at the end so that all beggars have a str associated with them
        print([int(coin) for coin in coins])                            # converting all the values in the string to integers so when print no " "
