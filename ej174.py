#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:06:20 2023

@author: maxilieban
"""
# ej 174

def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
    
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))


mcd1 = mcd(a, b)

print("El MCD entre", a, "y", b, "es", mcd1)



