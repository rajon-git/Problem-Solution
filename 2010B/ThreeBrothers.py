# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:39:35 2024

@author: Rajon
"""

def find_brothers(a,b):
    all_brothers = {1,2,3}
    
    arrived_brothers = {a,b}
    
    late = all_brothers - arrived_brothers
    
    print(late.pop())
a,b = map(int, input().split())

find_brothers(a,b)