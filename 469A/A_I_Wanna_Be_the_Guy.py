def can_pass_All_levels(x_levels,y_levels):
    x_levels_unique = set(x_levels)
    y_levels_unique = set(y_levels)
    all_possible_levels = x_levels_unique.union(y_levels_unique)

    if len(all_possible_levels) == n:
        return 'I become the guy.'
    else:
        return 'Oh, my keyboard!'
    
n = int(input().strip())
x_input = list(map(int, input().strip().split()))
y_input = list(map(int, input().strip().split()))

x_levels = x_input[1:]
y_levels = y_input[1:]
result = can_pass_All_levels(x_levels,y_levels)
print(result)