def divisibility_count(a,b):
    remainder = a % b
    if remainder == 0:
        return 0
    else:
        return b - remainder

n = int(input())

# Initialize an empty list to store results
results = []

# Process each test case
for _ in range(n):
    a, b = map(int, input().strip().split())
    result = divisibility_count(a, b)
    results.append(result)

# Print all results
for result in results:
    print(result)