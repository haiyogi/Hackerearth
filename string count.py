# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:02:10 2020

@author: K Yogesh
"""

t=int(input())
for i in range(t):
    s=input()
    s=s.replace("*"," ")
    s=s.upper()
    s=s.split()
    print(s)
    c=0
    for j in s:
        if "X" not in j:
            c=c+j.count("O")
    print(c)
    