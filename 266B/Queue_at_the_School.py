# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:07:12 2024

@author: Rajon
"""

def queue_at_school(n,t,s):
    queue = list(s)
    
    for _ in range(t):
        i = 0
        while i < n-1:
            if queue[i] == 'B' and queue[i+1] == 'G':
                queue[i], queue[i+1] = queue[i+1], queue[i]
                i += 1
            i += 1
            
    return ''.join(queue)

n, t = map(int, input().split())

s = input().strip()

result = queue_at_school(n,t,s)

print(result)

