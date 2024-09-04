def max_results(a,b,c):
    res1 = (a+b)*c
    res2 = a*(b+c)
    res3 = a*b*c
    res4 = a+b+c 

    return max(res1,res2,res3,res4)

a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

result= max_results(a,b,c)

print(result)