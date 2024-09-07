def min_swap_rearrange(n,heights):
    max_heights = max(heights)
    min_heights = min(heights)

    max_index = heights.index(max_heights)
    min_index = len(heights) - 1 - heights[::-1].index(min_heights)
    swaps = max_index + (n-1-min_index)
    if min_index < max_index:
        swaps -= 1
    return swaps

n= int(input().strip())
heights = list(map(int, input().strip().split()))
print(min_swap_rearrange(n,heights))