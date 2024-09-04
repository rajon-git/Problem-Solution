def min_road(h,heights):
    w = 0
    for height in heights:
        if height > h:
            w += 2
        else:
            w += 1
    return w

n,h = map(int, input().strip().split())
heights = list(map(int, input().split()))

result = min_road(h,heights)
print(result)