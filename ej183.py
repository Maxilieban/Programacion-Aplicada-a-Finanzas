#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:52:39 2023

@author: maxilieban
"""


# ej 183




def cadena(componentes, componente):
    
    for i in componentes:
    
        if componente != i:
            print("Ese componente no es valido")
           # return cadena(componentes, componente)
        
        else:
            
            if componente[-1] == componentes[i][0]:
                componente = componente + componentes[i]
                return cadena(componentes.remove(componentes[i]), componente[i])
 
    
 
#%%    
 
    
componentes = ['aluminio', 'plata', 'oro', 'cobre', 'calcio', 'mercurio', 'magnesio', 'carbono', 'oxigeno', 'hidrogeno', 'fluor', 'fosforo', 'yodo', 'helio', 'neon', 'argon', 'kripton', 'radon']
         
componente_usuario = input("Ingrese un componente quimico: ")

cadena_final = cadena(componentes, componente_usuario)        


def cadena(componentes, componente):
    
    for i in len(componentes):
        
        if componente == i:
        
            if componente[-1] == componentes[i][0]:
                componente = componente + componentes[i]
                return cadena(componentes.remove(componentes[i]), componentes[i])
            
            else:
                return componente 
        
        else:
            print("Ese componente no es valido")
            return cadena(componentes, componente)
        


    










    
    
    