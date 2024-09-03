def find_numbers(a, b):
    length = len(a)
    res = []

    for i in range(length):
        if a[i] != b[i]:
            res.append('1')
        else:
            res.append('0')
    return ''.join(res)

a = input().strip()
b = input().strip()
result = find_numbers(a, b)
print(result)
