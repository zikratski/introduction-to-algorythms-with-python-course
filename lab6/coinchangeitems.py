import sys

def getCoins(coins):
    return [int(i) for i in coins.split(',')]

def getGreedyCoins(coins, coins_sum):
    coins_change = []
    coins.sort()
    coins.reverse()
    for coin in coins:
        k = coins_sum//coin
        if k > 0:
            coins_change += [coin for _ in range(k)]
            coins_sum -= k*coin
    coins_change.reverse()
    if coins_sum or not coins_change:
        return float('inf'), list()
    else:
        return len(coins_change), coins_change

def getDynamicCoins(coins, coins_sum):
    coins.sort()
    coins_price = {i:func(i, coins) for i in range(coins_sum+1)}
    k = min(coins)
    for key in coins_price.keys():
        temp_dividers = list(filter(lambda x:x<= key,coins))
        if temp_dividers:
            versions = [(coins_price[key-i][0]+1,coins_price[key-i][1]+[i]) for i in temp_dividers]
            version = sorted(versions, key=lambda x:x[0])[0]
            coins_price[key] = [version[0],version[1]] if version[0] != float('inf') else [version[0],[]]
    return tuple(coins_price[coins_sum])
def func(i, coins):
    if i == 0:
        return [0,[]]
    if i in coins:
        return [1,[i]]
    else:
        return [float('inf'), []]

if __name__ == '__main__':
    coins = sys.argv[1]
    coins_sum = int(sys.argv[2])
    # coins = '2,6,7'
    # coins_sum = 5
    coins = getCoins(coins)
    greedy_coins = getGreedyCoins(coins, coins_sum)
    dynamic_coins = getDynamicCoins(coins, coins_sum)
    print(greedy_coins)
    print(dynamic_coins)