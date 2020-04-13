# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:08:39 2020

@author: K Yogesh
"""


T=int(input())
for i in range(T):
    string=list(input())
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    count=0
    for j in string:
        if(j=='('):
            a=a+1
        elif(j==')'):
            b=b+1
        elif(j=='['):
            c=c+1
        elif(j==']'):
            d=d+1
        elif(j=='{'):
            e=e+1
        elif(j=='}'):
            f=f+1
    if(a==b):
        count=count+(2*a)
    if(c==d):
        count=count+(2*c)
    if(e==f):
        count=count+(2*e)
    if(a!=b):
        if(a<b):
            count=count+(2*a)
        else:
            count=count+(2*b)
    if(c!=d):
        if(c<d):
            count=count+(2*c)
        else:
            count=count+(2*d)
    if(e!=f):
        if(e<f):
            count=count+(2*e)
        else:
            count=count+(2*f)
    print(count)