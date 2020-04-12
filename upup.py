# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:20:54 2020

@author: K Yogesh
"""


string = input()
a = []
for i in string.split(' '):
    a.append(i[:1].capitalize()+i[1:])
print(' '.join(a))