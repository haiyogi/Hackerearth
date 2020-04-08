# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:28:19 2020

@author: K Yogesh
"""


string = input()
count1,count2=0,0
for char in string:
    if(char == 'z'):
     count1+=1
    elif(char == 'o'):
     count2+=1
if(count2==(count1*2)):
  print('Yes')
else:
    print('No')
    
    
    