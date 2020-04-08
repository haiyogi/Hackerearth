# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:00:41 2020

@author: K Yogesh
"""


n=int(input())
for i in range(n):
    n-=i
    if n<=0:
        print("Patlu")
        break
    n-=(i*2)
    if n<=0:
        print('Motu')
        break