
import nltk.data
import os
from time import time

def devolverArchivos(ruta):
    sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    for archivo in os.listdir(ruta):
        archivo = open(os.path.join(ruta,archivo))
        cadena = archivo.read()
        sentences = sentence_tokenizer.tokenize(cadena)
        #print(sentences)
        print(archivo.name + " - Número de frases: " + str(len(sentences)))
            
start_time = time()
devolverArchivos("MCE-corpus")
elapsed_time = time() - start_time
print("Tiempo transcurrido: %.10f segundos." % elapsed_time)