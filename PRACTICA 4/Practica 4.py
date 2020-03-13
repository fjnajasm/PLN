from os import listdir
from os import path
from nltk import TreebankWordTokenizer
from nltk import data
from re import sub

tokenizer = TreebankWordTokenizer()
_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
tagger = data.load(_POS_TAGGER) 

reg = "[^\w]"

adv = 0
verb = 0
adj = 0
sust = 0

total = 0
for archivo in listdir("DIANN_Corpus"):
    archivo = open(path.join("DIANN_Corpus",archivo),'r',encoding = 'utf8')
    texto_archivo = archivo.read()
    tokens = tokenizer.tokenize(texto_archivo)
    filtrado = []
    for j in tokens:
        tmp = sub(reg,"",j)
        if tmp != '':
            filtrado.append(tmp)
    tags = tagger.tag(filtrado)
    total = total + len(tags)
    for j in tags:
        if j[1] == "RB" or j[1] == "RBR" or j[1] == "RBS":
            adv = adv + 1
        elif j[1] == "JJ" or j[1] == "JJR" or j[1] == "JJS":
            adj = adj + 1
        elif j[1] == "NN" or j[1] == "NNS" or j[1] == "NNP" or j[1] == "NNPS":
            sust = sust + 1
        elif j[1] == "VB" or j[1] == "VBD" or j[1] == "VBG" or j[1] == "VBN" or j[1] == "VBP" or j[1] == "VBZ":
            verb = verb + 1

print("Hay", adv, "adverbios, la proporcion es ", (adv/total)*100, "%")
print("Hay", verb, "verbos, la proporcion es ", (verb/total)*100, "%")
print("Hay", sust, "sustantivos, la proporcion es ", (sust/total)*100, "%")
print("Hay", adj, "adjetivos, la proporcion es ", (adj/total)*100, "%")