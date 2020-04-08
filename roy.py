# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:59:59 2020

@author: K Yogesh
"""


L = int(input())
N = int(input())
 
while(N):
    N -= 1
    W, H = map(int, input().split(' '))
    #print(W,H)
    if (W < L or H < L ):
        print('UPLOAD ANOTHER')
    elif(W>=L and H>=L):
        if (W == H):
            print('ACCEPTED')
        else:
            print('CROP IT')
 