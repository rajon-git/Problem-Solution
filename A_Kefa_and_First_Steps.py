def find_max_non_decreasing_length(n, a):
    if n == 0:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, n):
        if a[i] >= a[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
    
    # Final update for the last segment
    if current_length > max_length:
        max_length = current_length
    
    return max_length


n = int(input().strip())
a = list(map(int, input().strip().split()))

print(find_max_non_decreasing_length(n, a))