

from nltk.tokenize import TreebankWordTokenizer, WhitespaceTokenizer, SpaceTokenizer, WordPunctTokenizer

def tokenizarPorTipo():
    cadena = "Sorry, I can't go to the meeting.\n"
    print("TreebankWordTokenizer - 1")
    print("WhitespaceTokenizer - 2")
    print("SpaceTokenizer - 3")
    print("WordPunctTokenizer - 4")
    num = input("Introduzca un tokenizer: ")
    if num == "1":
        tokenizer = TreebankWordTokenizer()
    elif num == "2":
        tokenizer = WhitespaceTokenizer()
    elif num == "3":
        tokenizer = SpaceTokenizer()
    elif num == "4":
        tokenizer = WordPunctTokenizer()
    else:
        return
    
        
    tokens = tokenizer.tokenize(cadena)
    print(tokens)
  
while True:
    tokenizarPorTipo()
    print("\n")