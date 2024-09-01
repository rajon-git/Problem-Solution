# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:09:41 2024

@author: Rajon
"""

def tanya_subtractions(n,k):
    for _ in range(k):
        if n % 10 == 0:
            n //= 10
        else:
            n -= 1
    return n 

n, k = list(map(int, input().split()))

result = tanya_subtractions(n, k)
print(result)