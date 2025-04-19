n = int(input())
points = list(map(int, input().split()))
max_p = min_p = points[0]
count = 0

for p in points[1:]:
    if p > max_p:
        max_p = p
        count += 1
    elif p < min_p:
        min_p = p
        count += 1

print(count)