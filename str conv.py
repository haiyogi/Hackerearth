# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:46:14 2020

@author: K Yogesh
"""
refer="$abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(int(input())):
    string= input()
    ans=""
    for j in string:
        if j in refer:
            index=refer.find(j)
            if index > 26:
                index-=26
                ans+=str(index)
            else:
                ans+=str(index)
        else:
            ans+=refer[0]
    
    print(ans)
    