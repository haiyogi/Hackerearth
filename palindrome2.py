# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:41:32 2020

@author: K Yogesh
"""


def isPalindrome(s): 

    rev = ''.join(reversed(s)) 
 
    if (s == rev): 
        return True
    return False

t=int(input())
while(t>0):
    s = input()
    ans = isPalindrome(s) 
    if (ans): 
       print("YES",end=' ')
       if(len(s)%2==0):
           print("EVEN")
       else:
           print("ODD")
    else: 
       print("NO") 
    t=t-1