#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:47:43 2022

@author: sp
"""


number=int(input('input a number:'))

if number > 18:
    print('Adult')
elif number <=18 and number >9:
    print('Youth')
else:
    print('Kid')
