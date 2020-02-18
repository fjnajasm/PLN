import re

texto = "Sorry, I can't go to the meeting.\n"
patron = "[a-z]+'?[a-z]*"

tokens = re.findall(patron, texto, re.I)
print(tokens)