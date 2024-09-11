def numbers_of_min_taxi(n, groups):
   
    count = [0] * 5
    for g in groups:
        count[g] += 1
   
    taxis = count[4] 

    taxis += count[3]
    if count[1] > count[3]:
        count[1] -= count[3]
    else:
        count[1] = 0
    taxis += count[2] // 2
    if count[2] % 2 == 1:
        taxis += 1
        if count[1] >= 2:
            count[1] -= 2
        else:
            count[1] = 0
    if count[1] > 0:
        taxis += (count[1] + 3) // 4
    
    return taxis
n = int(input().strip())
groups = list(map(int, input().strip().split()))

print(numbers_of_min_taxi(n, groups))
