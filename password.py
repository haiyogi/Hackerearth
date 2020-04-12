# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:14:26 2020

@author: K Yogesh
"""


t=int(input())
a=[]
for i in range(t):
 n=input()
 rev=n[::-1]
 if rev in a:
  mid=len(n)//2
  print(str(len(n))+" "+n[mid])
  break
 else:
  a.append(n)
 
        
 