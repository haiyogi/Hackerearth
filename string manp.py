# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:42:11 2020

@author: K Yogesh
"""


a=input()
b=input()
l=0
if(len(a)==len(b)):
    if(a==b):
        print("YES")
 
    else:
        f=0
        for i in range(len(a)):
            l=ord(a[i])-ord(b[i])
            if(a[i]=='z' and l!=0):
                print("NO")
                f=1
                break
        if(f==0):
            
            print("YES")
else:
    print("NO")         