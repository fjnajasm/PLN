#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:02:32 2020

@author: fran
"""

def listas(a, b):
    lista_final = []
    for i in a:
        if(i not in lista_final) and (i in b):
            lista_final.append(i)
    return lista_final


def comprueba(a):
    try:
        for i in a:
            int(i)
        return True
    except ValueError:
        return False
            
lista1 = [1,2,3,4, 1,1,1,1,1,1,1,1]
lista2 = [1,3,4,5,6]

compruebaa = comprueba(lista1)
compruebab = comprueba(lista2)

res = []

if (compruebaa is True and compruebab is True):
    res = listas(lista1, lista2)

if len(res) == 0:
    print("Una de las listas no es de enteros completa")
else:
    for i in res:
        print(i)

