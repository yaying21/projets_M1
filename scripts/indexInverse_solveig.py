# -*- coding: utf-8 -*-

import os

from collections import Counter, defaultdict

corpus = defaultdict()
corpus["doc1"] = "le repas est pas mauvais"
corpus["doc2"] = "si, je le trouve pas bon"
corpus["doc3"] = "j’avoue il est vraiment mauvais"

dico = defaultdict(list)
tokens = defaultdict()
for cle, valeur in corpus.items():
    tokens[cle] = valeur.split(" ")
cnt = defaultdict(Counter)
for cle, valeur in tokens.items():
    for item in valeur:
        cnt[cle][item] += 1
        dico[item].append((cle, cnt[cle][item]))
        
        
for k in sorted(dico.keys()):
    print("%s: %s" % (k, dico[k]))
        
os.system("pause")

