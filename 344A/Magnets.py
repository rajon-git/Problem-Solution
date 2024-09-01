# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:00:38 2024

@author: Rajon
"""

def count_groups(n, magnets):
    if n == 0:
        return 0
    groups = 1
    current_orientation = magnets[0]
    
    for i in range(1,n):
        if magnets[i] != current_orientation:
            groups += 1
            current_orientation = magnets[i]
            
    return groups


n = int(input())
# magnets = list(input().split())
magnets = [input().strip() for _ in range(n)]

result = count_groups(n, magnets)
print(result)
