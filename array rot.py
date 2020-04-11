# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:37:48 2020

@author: K Yogesh
"""


for _ in range(int(input())):
    N,K= map(int,input().split())
    li=input().split()
    print(" ".join(li[N-(K%N):] + li[:N-(K%N)]))
    print("\n")