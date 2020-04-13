# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:49:04 2020

@author: K Yogesh
"""


l1=list(map(int,input()))
l2=list(map(int,input()))
c=0
c1=0
for i in range(len(l1)):
    if(l1[i]!=l2[i]):
        if(l2[i]==0):
            c=c+1
        elif(l2[i]==1):
            c1=c1+1
if(c==c1):
    print(c)
else:
    print("-1")