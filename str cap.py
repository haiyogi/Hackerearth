# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:24:45 2020

@author: K Yogesh
"""


str1=list(input())
n1,n2=map(int,input().split())
n1-=1
n2-=1
if(str1[n1].islower()):
    str1[n1]=str1[n1].upper()
else:
    str1[n1]=str1[n1].lower()
if(str1[n2].islower()):
    str1[n2]=str1[n2].upper()
else:
    str1[n2]=str1[n2].lower()
print("".join(str1))