# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:15:11 2024

@author: Rajon
"""

def trams_capacity(n, trams):
    current_passenger = 0
    max_capacity = 0
    
    for i in range(n):
        ai, bi = trams[i]
        current_passenger -= ai 
        current_passenger += bi 
        max_capacity = max(max_capacity, current_passenger)
        
    return max_capacity

n = int(input())
trams = [list(map(int, input().split())) for _ in range((n))]

result = trams_capacity(n, trams)

print(result)
