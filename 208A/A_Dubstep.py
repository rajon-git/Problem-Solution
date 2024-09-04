def dubstep_string(a):
    a = a.replace("WUB", " ")
    return ' '.join(a.split())

a= input().strip()

result = dubstep_string(a)
print(result)
