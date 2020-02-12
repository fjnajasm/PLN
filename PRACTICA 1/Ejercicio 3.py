#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 12:04:10 2020

@author: fran
"""

def genera_diccionario(cadena, solucion, diccionario):
    for carac in cadena:
        if carac == diccionario[0]:
            solucion[0] += 1
        if carac == diccionario[1]:
            solucion[1] += 1
        if carac == diccionario[2]:
            solucion[2] += 1
        if carac == diccionario[3]:
            solucion[3] += 1
        if carac == diccionario[4]:
            solucion[4] += 1
    return solucion



cadena = 'Esto es el ejercicio 3 de la practica 0 de PLN'
solucion = [0,0,0,0,0]
diccionario = ['a','e','i','o','u']

solucion = genera_diccionario(cadena,solucion,diccionario)

print("Para la cadena: " + cadena)

indice = 0
while indice < len(diccionario):
    print(diccionario[indice] + " : " + str(solucion[indice]))
    indice += 1
