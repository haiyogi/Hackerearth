# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:13:08 2020

@author: K Yogesh
"""


def isPossible(a, n): 
    sum = 0
    maxS = 0
    for i in range(n): 
        sum += a[i] 
        maxS = max(a[i], maxS) 

    if ((sum - maxS) > maxS): 
        return 1
      
    return -1
  

t= int(input())
while(t>0):
    
    s=int(input())
    L=list(map(int,input().split()))
    n = len(L)
    if(isPossible(L, n)==1):
        print("Yes")
    else:
        print("No")
    t-=1
    
    
    
    
    
    
 
