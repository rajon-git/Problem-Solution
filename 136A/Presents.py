# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:18:39 2024

@author: Rajon
"""

def find_giver(friends, receivers):
    
    result = [0] * friends
    
    for giver in range(friends):
        receiver = receivers[giver] - 1
        result[receiver] = giver + 1
    
    return result

friends = int(input())
receivers = list(map(int,input().split()))

giver_gift = find_giver(friends, receivers)

print(" ".join(map(str, giver_gift)))
