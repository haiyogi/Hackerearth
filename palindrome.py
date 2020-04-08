# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:57:42 2020

@author: K Yogesh
"""


str1=input()
str1=str1.casefold()

str2=reversed(str1)

if list(str1)==list(str2):
    print('YES')
else:
    print('NO')