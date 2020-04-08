# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:53:55 2020

@author: K Yogesh
"""


string = input()
string=string.lower()
count,count1=0,0
for i in string:
    if (i=='r'):
        count+=1
    elif(i=='l'):
        count-=1
    elif(i=='u'):
        count1+=1
    elif(i=='d'):
        count1-=1
print(count,count1)
        
        