# -*- coding: utf-8 -*-
#Anaëlle Pierredon

index= {}


documents = {
    "doc1" : "La bouffe est pas mauvaise",
    "doc2" : "Si, je le trouve pas bon",
    "doc3" : "J'avoue il est vraiment mauvais"
    }

for item in documents :
    liste = documents[item].split()
    for word in liste:
        if word in index:
            n = len(index[word])-1
            if item == index[word][n][0] :
                index[word][n] = (index[word][n][0], index[word][n][1]+1)
            else:
                index[word].append((item , 1))
            
        else:
            index[word] = [(item , 1)]
        
for cle, valeur in index.items():
    print(f"{cle} : {valeur}")
