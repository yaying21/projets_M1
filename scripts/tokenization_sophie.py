#Sophie REPINGON
#tokenization_sophie.py
#-*- coding : utf-8 -*-

from collections import Counter, defaultdict

import spacy
from spacy import displacy
nlp = spacy.load('fr_core_news_sm')

import nltk
from nltk.corpus import stopwords

dico_docs = {"doc1" : nlp("la bouffe est pas mauvaise"), 
             "doc2" : nlp("si, je le trouve pas bon"), 
             "doc3" : nlp("j'avoue il est vraiment vraiment mauvais")}

dico_words = defaultdict(list)

for document, phrase in dico_docs.items():
    compteur = Counter()
    for token in phrase:
        if token.pos_ == "PUNCT": #On enlève la ponctuation
            continue
        if token.text in stopwords.words('french'): #Stopwordisation
            continue
        lemme = token.lemma_ #Lemmatisation
        pos = token.pos_ #Postagging
        compteur[lemme,pos]+=1
    for lemme, frequence in compteur.items():
        dico_words[lemme].append((document, frequence))
        
for lemme in dico_words:
    print(f'{lemme} : {dico_words[lemme]} ')


