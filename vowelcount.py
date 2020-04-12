# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:43:14 2020

@author: K Yogesh
"""

t=int(input())

while(t>0):
    t=t-1
    count=0
    string =input()
    string=string.lower()
    string = list(string)
    for char in string:
        if(char == 'a'):
           count+=1
        elif(char=='e'):
           count+=1
        elif(char=='i'):
           count+=1
        elif(char=='o'):
           count+=1
        elif(char=='u'):
           count+=1
    print(count)    

