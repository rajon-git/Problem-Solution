def draw_snake(n,m):
    for r in range(n):
        if r%2 == 0:
            print('#' * m)
        else:
            if (r // 2) % 2 ==0:
                print('.' * (m - 1) + '#')
            else: 
                print('#' + '.' * (m - 1))

n, m = map(int, input().split())
draw_snake(n,m)