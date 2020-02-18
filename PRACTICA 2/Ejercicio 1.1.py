
from nltk.tokenize import sent_tokenize
import os
from time import time

def devolverArchivos(ruta):
    for archivo in os.listdir(ruta):
        archivo = open(os.path.join(ruta,archivo))
        cadena = archivo.read()
        frase = sent_tokenize(cadena)
        print(archivo.name + " - Número de frases: " + str(len(frase)))
            

start_time = time()
devolverArchivos("MCE-corpus")
elapsed_time = time() - start_time
print("Tiempo transcurrido: %.10f segundos." % elapsed_time)