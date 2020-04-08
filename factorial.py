# # -*- coding: utf-8 -*-
# """
# Created on Wed Apr  8 16:03:28 2020

# @author: K Yogesh
# """


# n = int(input())
# fact=1
# arr = int(input())
# for i in arr:
#     fact =(fact * arr[i])%(10**9+7)

# print(fact)    
x=int(input())
y=input()
z=y.split(" ")
c=1
for k in z:
    c=(c*int(k))%(10**9+7)
print(c)
 