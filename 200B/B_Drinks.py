def average_of_orange_coctail(n,percentes):
    total_percentages = sum(percentes)

    avg = total_percentages/n
    return avg 

n = int(input().strip())
percentes = list(map(int, input().strip().split()))

result = average_of_orange_coctail(n, percentes)
print(f"{result:.12f}")