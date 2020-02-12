#Sophie REPINGON
#indexinverse_sophie.py
#-*- coding : utf-8 -*-

from collections import Counter

dico_docs = {"doc1" : "la bouffe est pas mauvaise", 
             "doc2" : "si, je le trouve pas bon", 
             "doc3" : "j'avoue il est vraiment mauvais"}

dico_words = {}

for k, v in dico_docs.items():
    compteur = Counter()
    mots = v.split()
    for item in mots:
        if item not in dico_words.keys():
            compteur[item] +=1
            dico_words[item] = (k, compteur[item])   
        else:
            compteur[item] +=1
            dico_words[item] = (dico_words[item], k, compteur[item])

print(dico_words)