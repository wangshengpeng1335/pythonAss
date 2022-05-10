#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:53:45 2022

@author: sp
"""


contacts = {'Kim': '010-111-1234', 'Park': '010-222-2345', 'Lee': '010-333-3456'}

a = input("Enter friends name:")
if a == 'Kim':
   print(contacts['Kim'])
elif a=='Park':
       print(contacts['Park'])
elif a=='Lee':
        print(contacts['Lee'])
else:
    print("None")