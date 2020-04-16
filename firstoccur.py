# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:55:36 2020

@author: K Yogesh
"""


def program():
    s=input()
 
    unique = []
    occurenceset = set()
 
    for x in s:
        if x not in occurenceset:
            unique.append(x)
            occurenceset.add(x)
 
    for x in unique:
        print(x,end="")
    print()
 
for i in range(int(input())):
    program()