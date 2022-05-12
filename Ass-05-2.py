#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:08:45 2022

@author: sp
"""


a =int(input('enter tan integer:'))
b = int(input('enter tan integer:'))
c = int(input('enter tan integer:'))
d = int(input('enter tan integer:'))

e =[a,b,c,d]
f = sorted(set(e),reverse=True)
f.remove(max(f))
print("the max is",max(e))
print(f)

##this is Q5 test 20220426  n 2
##this is Q1 test 20220426  n0 1