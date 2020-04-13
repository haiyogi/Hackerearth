# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:14:39 2020

@author: K Yogesh
"""


s=list(input().split())
new=''
for i in range(len(s)-1):
    new+=(s[i][0])+'.'
    new+=' '
new+=s[-1]
print(new)