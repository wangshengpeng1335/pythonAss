#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:07:41 2022

@author: sp
"""



list = []

def the_input(count=eval(input("Enter the total number of multipliers:"))):

    for i in range(count):
        N=eval(input("input number:"))
        list.append(N)
    print("total:",count)
    print("multiply:",list)


the_input()

def multiply(*num):
    sum =1
    for n in num:
        sum = sum * n
    return sum

print("result：",multiply(*list))



##this is Q5 test 20220426  n 3


 

 

 
