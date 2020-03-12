
archivo_austen = "austen-sense.txt"
archivo_carroll = "carroll-alice.txt"
archivo_cherteston = "chesterton-brown.txt"

archivo_auste = open(archivo_austen)
archivo_carroll = open(archivo_carroll)
archivo_cherteston = open(archivo_cherteston)

cadena_auste = archivo_auste.read()
cadena_carroll = archivo_carroll.read()
cadena_cherteston = archivo_cherteston.read()


print(cadena_auste)
print(cadena_carroll)
print(cadena_cherteston)