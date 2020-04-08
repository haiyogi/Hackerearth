# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:31:56 2020

@author: K Yogesh
"""


x=int(input())
y=int(input())
z=int(input())
count=0
for i in range(x,y+1):
    if(i%z==0):
      count+=1
print(count)