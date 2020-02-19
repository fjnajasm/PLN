
from nltk.tokenize import sent_tokenize
import os
from time import time
from bs4 import BeautifulSoup

#Considero el summay y el body

def devolverArchivos(ruta):
    totalOraciones = 0
    numArchivos = 0
    for archivo in os.listdir(ruta):
        archivo = open(os.path.join(ruta,archivo))
        cadena = archivo.read()
        cadena = BeautifulSoup(cadena, "lxml").text
        frase = sent_tokenize(cadena)
        print(archivo.name + " - Número de frases: " + str(len(frase)))
        numArchivos += 1
        totalOraciones += len(frase)
    media = totalOraciones / numArchivos
    print("La media es: " + str(media))
            

start_time = time()
devolverArchivos("MCE-corpus")
elapsed_time = time() - start_time
print("Tiempo transcurrido: %.10f segundos." % elapsed_time)