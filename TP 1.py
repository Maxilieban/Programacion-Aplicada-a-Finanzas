#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:24:27 2023

@author: maxilieban
"""

class Myarray1:
    

    def __init__(self, elems, r, c, by_row):
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
        
        
    def get_pos(self, j, k):   # en la matriz, tanto para filas como columnas, el primer indice de las coordenadas es 0.      
        """Esta funcion toma como argumentos a j(numero de fila) y k(numero de columna)
        correspondientes a la matriz y devuelve el indice correspondiente de la lista
        para ese elemento."""
        
        if (type(j) != int) or (type(k) != int) or (j < 0) or (k < 0):
            raise ValueError("j and k must be positive integers.")
    
        if j < self.r and k < self.c:
            
            if self.by_row:
                indice = elems.index(elems[j*self.c+k])
                print(f"El indice de la lista correspondiente a las coordenadas ({j}, {k}) es: {indice}.")
                
            else:
                indice = elems.index(elems[k*self.r+j])
                print(f"El indice de la lista correspondiente a las coordenadas ({j}, {k}) es: {indice}.")
          
            return indice
        
        else:
            raise IndexError("Coordinates out of range.")
        
            
    def get_coords(self, m):
        """Esta funcion toma como argumento a m (indice correspondiente a la
        lista) y devuelve los indices (j, k) correspondientes a los indices
        en la matriz."""
        
        if type(m) != int:
            raise ValueError("m must be an integer.")
        
        if m <= len(self.elems):
            
            if self.by_row:      
                coord_j = m // self.r
                coord_k = m % self.c
                tupla_coordenadas = (coord_j, coord_k)
                print(f"Las coordenadas para el elemento cuyo indice en la lista es {m} son: ({coord_j}, {coord_k}).")
           
            else:
                coord_j = m // self.c
                coord_k = m % self.r
                tupla_coordenadas = (coord_j, coord_k)
                print(f"Las coordenadas para el elemento cuyo indice en la lista es {m} son: ({coord_j}, {coord_k}).")
                
            return tupla_coordenadas
    
        else:
            raise IndexError("Index out of range.")
        
        
    def switch(self):
        """Esta funcion altera la lista elems y modifica el valor de by_row."""
             
        elems_a_modificar = self.elems.copy()
        elems_modificada = []
        for i in range(self.c):
            elems_modificada += elems_a_modificar[i::self.c]
        elems_a_modificar = elems_modificada
        
        if self.by_row:
            self.by_row = False
            
        else:
            self.by_row = True
                    
        return elems_a_modificar
    
    
    def get_row(self, j):
        """Esta funcion toma como argumento a j (numero de fila en la matriz) 
        y devuelve una lista con esa fila."""
        
        if type(j) != int:
            raise ValueError("j must be an integer.")
        
        if j < r:
        
            if self.by_row:           
                lista_elementos_row = self.elems[j*self.c:(j+1)*self.c:]
                return lista_elementos_row
        
            else: 
                lista_elementos_row = self.elems[j::self.c]
                return lista_elementos_row
        
        else:
            raise IndexError("Index j out of range.")
        
            
    def get_col(self, k):
        """Esta funcion toma como argumento a k (numero de columna en la matriz) 
        y devuelve una lista con esa columna."""
                
        if type(k) != int:
            raise ValueError("k must be an integer.")
        
        if k < c:
            
            if self.by_row:
                lista_elementos_column = self.elems[k::self.c]
                return lista_elementos_column
            
            else:
                lista_elementos_column = self.elems[k*self.c:(k+1)*c:]
                return lista_elementos_column
            
        else:
            raise IndexError("Index k out of range.")
        
        
    def get_elem(self, j, k):
        """Esta funcion toma como argumento a j y k (numero de fila y columna
        en la matriz) y devuelve el elemento correspondiente."""
            
        if (type(j) != int) or (type(k) != int) or (j < 0) or (k < 0):
            raise ValueError("j and k must be positive integers.")
    
        if j < self.r and k < self.c:
                
            if self.by_row:
                elemento = elems[j*self.c+k]
                print(f"El elemento correspondiente a las coordenadas ({j}, {k}) es: {elemento}.")
                    
            else:
                elemento = elems[k*self.r+j]
                print(f"El elemento correspondiente a las coordenadas ({j}, {k}) es: {elemento}.")
              
            return elemento
            
        else:
            raise IndexError("Coordinates out of range.")
               
            
    def del_row(self, j):
        """Esta funcion toma como argumento a j (numero de fila en la matriz) 
        y devuelve una lista sin esa fila."""
        
        if type(j) != int:
            raise ValueError("j must be an integer.")
            
        if j < self.r:
            
            if self.by_row:     
                elems_nueva = self.elems.copy()
                del elems_nueva[j*self.c:(j+1)*self.c:]
                return elems_nueva
            
            else:
                elems_nueva = self.elems.copy()
                del elems_nueva[j::self.c]
                return elems_nueva
                    
        else:
            raise IndexError("Index j out of range.")    
            
    
    def del_col(self, k):
        """Esta funcion toma como argumento a k (numero de columna en la matriz) 
        y devuelve una lista sin esa columna."""
        
        if type(k) != int:
            raise ValueError("k must be an integer.")
            
        if k < self.c:
            
            if self.by_row:     
                elems_nueva = self.elems.copy()
                del elems_nueva[k::self.c]
                return elems_nueva
                
            else:
                elems_nueva = self.elems.copy()
                del elems_nueva[k*self.c:(k+1)*self.c:]
                return elems_nueva
            
        else:
            raise IndexError("Index k out of range.")
                             
    
    def swap_rows(self, j, k):
        """Esta funcion toma como argumentos a j y k (dos filas de la matriz)
        y devuelve una lista con esas filas intercambiadas de posicion."""
        
        if type(j) != int or type(k) != int:
            raise ValueError("j and k must be integers.")
            
        if j < self.r and k < self.r:
            elems_swapped_rows = self.elems.copy()
            elems_swapped_rows[j*self.c:(j+1)*self.c:], elems_swapped_rows[k*self.c:(k+1)*self.c:] = elems_swapped_rows[k*self.c:(k+1)*self.c:], elems_swapped_rows[j*self.c:(j+1)*self.c:]
            
        else:
            raise IndexError("Index out of range.")
        
        return elems_swapped_rows
    
    
    def swap_cols(self, m, l):
        """Esta funcion toma como argumentos a j y k (dos columnas de la matriz)
        y devuelve una lista con esas columnas intercambiadas de posicion."""
        
        if type(m) != int or type(l) != int:
            raise ValueError("m and l must be integers.")
            
        if m <= self.c and l <= self.c:
            elems_swapped_cols = self.elems.copy()
            elems_swapped_cols[m::c], elems_swapped_cols[l::c] = elems_swapped_cols[l::c], elems_swapped_cols[m::c]
        
        else:
            raise IndexError("Index out of range.")
        
        return Myarray1(elems_swapped_cols, self.r, self.c, self.by_row)
    
    
    def scale_row(self, j, x):
        """Esta funcion toma como argumentos a j (fila de la matriz) y x (numero)
        y devuelve una lista con esa fila multiplicada por x. """
        
        if type(j) != int or (type(x) != int and type(x) != float):
            raise ValueError("j must be an integer and x must be integer or float.")
        
        if j < self.r:
            
            if self.by_row:
                elems_scale_row = self.elems.copy()
                for element in range(j*self.c, (j+1)*self.c):
                    elems_scale_row[element] *= x
                return elems_scale_row
                
            else:
                elems_scale_row = self.elems.copy()
                for element in range(j, len(elems_scale_row) , self.c):
                    elems_scale_row[element] *= x
                return elems_scale_row
        
        else:
            raise IndexError("Index j out of range.")
            
            
    def scale_col(self, k, y):
        """Esta funcion toma como argumentos a j (columna de la matriz) y y (numero)
        y devuelve una lista con esa fila multiplicada por x. """
        
        if type(k) != int or (type(y) != int and type(y) != float):
            raise ValueError("j must be an integer and x must be integer or float.")
        
        if k < self.c:
            
            if self.by_row:
                elems_scale_row = self.elems.copy()
                for element in range(k, len(elems_scale_row) , self.c):
                    elems_scale_row[element] *= y
                return elems_scale_row
                
            else:
                elems_scale_row = self.elems.copy()
                for element in range(k*self.c, (k+1)*self.c):
                    elems_scale_row[element] *= y
                return elems_scale_row
        
        else:
            raise IndexError("Index k out of range.")
        
    
    def transpose(self):
        """Esta funcion devuelve una lista que representa a la matriz transpuesta."""
        
        elems_a_transponer = self.elems.copy()
        transposed = []
        for i in range(self.c):
            transposed += elems_a_transponer[i::self.c]
        elems_a_transponer = transposed
        return elems_a_transponer
            
        
    def flip_rows(self):
        """Esta funcion devuelve una copia de la lista pero reflejando especularmente
        sus filas."""
        
        flipped_elems = []
        for e in range(self.r, -1, -1):
            flipped_elems.extend(self.get_row(e))       
        return flipped_elems
        
        
    def flip_cols(self):
        """Esta funcion devuelve una copia de la lista pero reflejando especularmente
        sus columnas."""
        
        flipped_elems = []
        for e in range(0, self.r):
            row = self.elems[e * self.c : (e + 1) * self.c]
            flipped_elems.extend(row[::-1])
        return flipped_elems
    
    
  #  def det(self):
        
elems = [0, 1, 2, 3, 4, 5, 6, 7, 8]
r = 3
c = 3
 
x = Myarray1(elems, r, c, by_row = True)


#%%


class Myarray2:
    

    def __init__(self, elems, r, c, by_row):
        self.elems = elems
        self.r = r
        self.c = c
        self.by_row = by_row
        
        self.new_elems = []
        for i in range(self.r):
            row = []
            for j in range(self.c):
                index = i * self.c + j
                row.append(self.elems[index])
            self.new_elems.append(row)
        
        
    def get_pos(self, j, k):   
        """Esta funcion toma como argumentos a j(numero de fila) y k(numero de columna)
        correspondientes a la matriz y devuelve el indice correspondiente de la lista
        para ese elemento."""
        
        if (type(j) != int) or (type(k) != int) or (j < 0) or (k < 0):
            raise ValueError("j and k must be positive integers.")
    
        if j <= self.r and k <= self.c:
            
            if self.by_row:
                indice = self.new_elems.index(self.new_elems[j][k])
                print(f"El indice de la lista correspondiente a las coordenadas ({j}, {k}) es: {indice}.")
                
            else:
                indice = self.new_elems.index(self.new_elems[k][j])
                print(f"El indice de la lista correspondiente a las coordenadas ({j}, {k}) es: {indice}.")
          
            return indice
        
        else:
            raise IndexError("Coordinates out of range.")
        
            
    def get_coords(self, m):
        """Esta funcion toma como argumento a m (indice correspondiente a la 
        lista) y devuelve los indices (j, k) correspondientes a los indices
        en la matriz."""
        
        if type(m) != int:
            raise ValueError("m must be an integer.")
        
        if m <= len(self.elems):
            
            if self.by_row:      
                coord_j = m // self.r
                coord_k = m % self.c
                tupla_coordenadas = (coord_j, coord_k)
           
            else:
                coord_j = m // self.c
                coord_k = m % self.r
                tupla_coordenadas = (coord_j, coord_k)
                print(f"Las coordenadas para el elemento cuyo indice en la lista es {m} son: ({coord_j}, {coord_k}).")
                
            return tupla_coordenadas
    
        else:
            raise IndexError("Index out of range.")
        
        
    # def switch(self): 
    #     """Esta funcion altera la lista elems y modifica el valor de by_row."""
             
    
    def get_row(self, j):
        """Esta funcion toma como argumento a j (numero de fila en la matriz) 
        y devuelve una lista con esa fila."""
        
        if type(j) != int:
            raise ValueError("j must be an integer.")
        
        if j < r:
        
            if self.by_row:           
                lista_elementos_row = self.new_elems[j]               
        
            else: 
                lista_elementos_row = []
                for i in range(self.new_elems):                    
                    lista_elementos_row.append(self.new_elems[i][j])
            return lista_elementos_row
        
        else:
            raise IndexError("Index j out of range.")
        
            
    def get_col(self, k):
        """Esta funcion toma como argumento a k (numero de columna en la matriz) 
        y devuelve una lista con esa columna."""
                
        if type(k) != int:
            raise ValueError("k must be an integer.")
        
        if k < c:
            
            if self.by_row:
                lista_elementos_column = []
                for i in range(len(self.new_elems)):
                    lista_elementos_column.append(self.new_elems[i][k])
            
            else:
                lista_elementos_column = self.new_elems[k]
            return lista_elementos_column
            
        else:
            raise IndexError("Index k out of range.")
        
        
    def get_elem(self, j, k):
        """Esta funcion toma como argumento a j y k (numero de fila y columna
        en la matriz) y devuelve el elemento correspondiente."""
            
        if (type(j) != int) or (type(k) != int) or (j < 0) or (k < 0):
            raise ValueError("j and k must be positive integers.")
    
        if j < self.r and k < self.c:
                
            if self.by_row:
                elemento = self.new_elems[j][k]
                print(f"El elemento correspondiente a las coordenadas ({j}, {k}) es: {elemento}.")
                    
            else:
                elemento = self.new_elems[k][j]
                print(f"El elemento correspondiente a las coordenadas ({j}, {k}) es: {elemento}.")
              
            return elemento
            
        else:
            raise IndexError("Coordinates out of range.")
               
            
    def del_row(self, j):
        """Esta funcion toma como argumento a j (numero de fila en la matriz) 
        y devuelve una lista sin esa fila."""
        
        if type(j) != int:
            raise ValueError("j must be an integer.")
            
        if j < self.r:
            
            if self.by_row:     
                elems_nueva = self.new_elems.copy()
                del elems_nueva[j]
                return elems_nueva
            
            else:
                elems_nueva = self.new_elems.copy()
                for i in range(self.new_elems):
                    del elems_nueva[i][j]
                return elems_nueva
                    
        else:
            raise IndexError("Index j out of range.")    
            
    
    def del_col(self, k):
        """Esta funcion toma como argumento a k (numero de columna en la matriz) 
        y devuelve una lista sin esa columna."""
        
        if type(k) != int:
            raise ValueError("k must be an integer.")
            
        if k < self.c:
            
            if self.by_row:     
                elems_nueva = self.new_elems.copy()
                for i in range(len(self.new_elems)):
                    del elems_nueva[i][k]
                return elems_nueva
                
            else:
                elems_nueva = self.new_elems.copy()
                del elems_nueva[k]
                return elems_nueva
            
        else:
            raise IndexError("Index k out of range.")
                             
    
    # def swap_rows(self, j, k):  
    #     """Esta funcion toma como argumentos a j y k (dos filas de la matriz)
    #     y devuelve una lista con esas filas intercambiadas de posicion."""
    
    
    # def swap_cols(self, m, l): 
    #     """Esta funcion toma como argumentos a j y k (dos columnas de la matriz)
    #     y devuelve una lista con esas columnas intercambiadas de posicion."""
        
    
    # def scale_row(self, j, x):
    #     """Esta funcion toma como argumentos a j (fila de la matriz) y x (numero)
    #     y devuelve una lista con esa fila multiplicada por x. """
        
      
            
            
    # def scale_col(self, k, y):
    #     """Esta funcion toma como argumentos a j (columna de la matriz) y y (numero)
    #     y devuelve una lista con esa fila multiplicada por x. """
        
        
        
    
    # def transpose(self):
    #     """Esta funcion devuelve una lista que representa a la matriz transpuesta."""
        
        
        
    # def flip_rows(self):
    #     """Esta funcion devuelve una copia de la lista pero reflejando especularmente
    #     sus filas."""
        
        
        
    # def flip_cols(self):
    #     """Esta funcion devuelve una copia de la lista pero reflejando especularmente
    #     sus columnas."""
        
    
    # def det(self):
        
        
      


        
elems = [0, 1, 2, 3, 4, 5, 6, 7, 8]
r = 3
c = 3
 
y = Myarray2(elems, r, c, by_row = True)
