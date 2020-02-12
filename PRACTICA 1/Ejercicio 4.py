# -*- coding: utf-8 -*-
"""
Ejercicio 4 - Francisco Jesús Najas Martos

Práctica 1 PLN

"""

from itertools import *

def genera_archivo(fichero1, fichero2):
    archivo = open("fichero_suma.txt", "w")
    c = map(sum, zip_longest(fichero1, fichero2, fillvalue=0))
    for i in c:
        print(i)
        archivo.write(str(i) + "\n")
        
a = []
b = []

fichero1 = open("fichero1.txt", "r")
fichero1.seek(0)
for linea in fichero1.readlines():
    try:
        a.append(int(linea))
    except ValueError:
        a.append(0)
    
fichero2 = open("fichero2.txt", "r")
fichero2.seek(0)
for linea in fichero2.readlines():
    try:
        b.append(int(linea))
    except ValueError:
        b.append(0)
    
genera_archivo(a,b)