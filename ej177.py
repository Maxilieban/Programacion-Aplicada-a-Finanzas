#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:47:41 2023

@author: maxilieban
"""


# ej 177


def number(roman):
    
    if roman == "":
        return 0
    
    else:
        valores = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        if len(roman) == 1:
            return valores[roman]
        
        if valores[roman[0]] < valores[roman[1]]:
            return valores[roman[1]] - valores[roman[0]] + number(roman[2::])
        
        else:
            return valores[roman[1]] + valores[roman[0]] + number(roman[2::])
        
roman = str(input("Numero romano: "))

numero_entero = number(roman)

print("El numero romano", roman, "escrito como entero es:", numero_entero)

            

        