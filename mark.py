# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:39:28 2020

@author: K Yogesh
"""


n,k=map(int,input().split())
l=list(map(int,input().split()))
skip=0
c=0
for i in l:
    if i<=k and skip<2:
        c+=1
    else:
        skip+=1
print(c)