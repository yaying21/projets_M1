# -*- coding: utf-8 -*-
#Index_inverse - Juliette Caron

from collections import defaultdict, Counter
from nltk.tokenize import word_tokenize

dico = defaultdict(list)

phrases = {"doc1" : "La bouffe est pas mauvaise", "doc2" : "Si, je le trouve pas bon", "doc3" : "J'avoue il est vraiment mauvais"}

for doc in phrases :
    ct = Counter()
    for token in word_tokenize(phrases[doc].lower()) :
        ct[token]+=1
    for token_c in ct :
        dico[token_c].append((doc, ct[token_c]))
            
for mot in dico :
    print (f"{mot} : {dico[mot]}")