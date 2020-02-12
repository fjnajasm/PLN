# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"EJERCICIO 1"
while True:
    try:
        print("Introduzca un valor:")
        entrada = input()
        
        while int(entrada) % 2 != 0:
            print("Introduzca un valor:")
            entrada = input()
        
        break
    except ValueError:
        0
    
print(entrada, "es un numero par");