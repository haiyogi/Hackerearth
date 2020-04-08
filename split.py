# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:51:06 2020

@author: K Yogesh
"""


x = int(input()) 
string = input()
i = 0
flag = 0
while i < len(string)-1:
    if string[i] == 'H' and string[i+1] == 'H':
        flag = -1
        print("NO")
        break
    i += 1
 
if flag == 0:
    string = string.replace('.','B')
    print("YES")
    print(string)