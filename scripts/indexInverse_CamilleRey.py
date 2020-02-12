# coding: utf-8 -Camille rey - version liste de tuples

from collections import Counter , defaultdict

corpus={"doc1":"la bouffe est pas mauvaise","doc2":"si, je le trouve pas bon","doc3":"j'avoue il est pas mauvaise"}

index_inv=defaultdict(list)

for doc,contenu in corpus.items():
       mot_fq=Counter()
       for mot in contenu.split():
              mot_fq[mot]+=1
       for mot,fq in mot_fq.items():
              index_inv[mot].append((doc,fq))

[print(f"{mot} : {index_inv[mot]}") for mot in index_inv]
    
