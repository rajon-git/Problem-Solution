
def min_coin_finders(n,coins):
    total = sum(coins)
    half = total/2 
    sorted_coins = sorted(coins, reverse=True)

    current_sum = 0
    count = 0

    for coin in sorted_coins:
        current_sum += coin
        count += 1
        if current_sum > half:
            return count
    return count

n = int(input())
coins = list(map(int,input().split()))

result = min_coin_finders(n,coins)
print(result)