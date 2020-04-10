# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:53:21 2020

@author: K Yogesh
"""
t=int(input())
for _ in range(t):
    n=input()
    l=list(n)
    l.sort()
    n1=len(l)
    c=0
    for i in range(n1-1):
        if abs(int(l[i])-int(l[i+1]))==1:
            c+=1
    
    if c==n1-1:
        print("YES")
    else:
        print("NO")
 