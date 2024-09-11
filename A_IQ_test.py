def count_evenless_numbers(n, numbers):
    evens = []
    odds = []

    for i in range(n):
        if numbers[i] % 2 == 0:
            evens.append(i+1)
        else:
            odds.append(i+1)

    if len(evens) == 1:
        return evens[0]
    else:
        return odds[0]

n = int(input().strip())
numbers = list(map(int,input().strip().split()))

print(count_evenless_numbers(n, numbers))