def count_damaged_dragon(k,l,m,n,d):
    damaged = [False] * (d+1)

    for i in range(k, d+1, k):
        damaged[i] = True
    for i in range(l, d+1, l):
        damaged[i] = True
    for i in range(m, d+1, m):
        damaged[i] = True 
    for i in range(n, d+1, n):
        damaged[i] = True
    
    count = sum(damaged)
    return count

k= int(input().strip())
l= int(input().strip())
m= int(input().strip())
n= int(input().strip())
d= int(input().strip())

print(count_damaged_dragon(k,l,m,n,d))