def find_minimum(colors):
    unique_color = set(colors)
    unique_count = len(unique_color)

    return 4- unique_count

colors = list(map(int, input().strip().split()))

result = find_minimum(colors)

print(result)