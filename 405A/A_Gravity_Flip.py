def gravity_of_cubes(n, cubes):
    # Sort the list of cubes
    sorted_cubes = sorted(cubes)
    # Convert each integer to a string and join them with a space separator
    result = ' '.join(map(str, sorted_cubes))
    return result

# Read input
n = int(input().strip())
cubes = list(map(int, input().strip().split()))

# Get the result and print it
result = gravity_of_cubes(n, cubes)
print(result)
