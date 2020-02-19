import re

texto = "Expresión at 5 pm can't"
patron = "\w+'?\w*"

tokens = re.findall(patron, texto)
print(tokens)