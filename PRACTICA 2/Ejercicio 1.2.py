
import nltk.data
import os
from time import time
from bs4 import BeautifulSoup

#Considero el summary y el body en los archivos

def devolverArchivos(ruta):
    sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    totalOraciones = 0
    numArchivos = 0
    for archivo in os.listdir(ruta):
        archivo = open(os.path.join(ruta,archivo))
        cadena = archivo.read()
        cadena = BeautifulSoup(cadena,"lxml").text
        sentences = sentence_tokenizer.tokenize(cadena)
        print(archivo.name + " - Número de frases: " + str(len(sentences)))
        numArchivos += 1
        totalOraciones += len(sentences)
    media = totalOraciones / numArchivos
    print("La media de oraciones es: " + str(media))
            
start_time = time()
devolverArchivos("MCE-corpus")
elapsed_time = time() - start_time
print("Tiempo transcurrido: %.10f segundos." % elapsed_time)