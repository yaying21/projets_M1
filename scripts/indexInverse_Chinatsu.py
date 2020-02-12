# -*- coding: utf-8 -*-

# Cours 2 06/02/2020  - Index inversé 
#Chinatsu KUROIWA

from collections import Counter , defaultdict

p1 = "la bouffe est pas mauvaise."
p2 = "Si, je la trouve pas bonne."
p3 = "J'avoue elle est vraiment mauvaise."
corpus = {"doc1":p1,"doc2":p2,"doc3":p3}


def index_inverse(doc):

	dict_idInverse = defaultdict(list)
	
	for key,val in doc.items():
		for token in val.split(' '):
			dict = Counter({})
			dict[token] += 1
			for cle,valu in dict.items():
				dict_idInverse[cle].append((key,valu))
	return (dict_idInverse)

result = index_inverse(corpus)
for key,val in sorted(result.items(), key=lambda x: x[0]):
	print (f"'{key}' : {val}")
	
 