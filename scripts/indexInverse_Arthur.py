#utf-8

from collections import defaultdict

doc1 = "La la bouffe est pas mauvaise"
doc2 = "Si je la trouve pas bonne la bouffe"
doc3 = "J avoue elle est vraiment mauvaise la bouffe"
doc4 = "elle elle est pas si mauvaise je trouve moi moi la bouffe"

sentences = [("doc1", doc1), ("doc2", doc2), ("doc3",doc3), ("doc4", doc4)]

dico2 = defaultdict(list)

for doc in sentences :
	dico = {}
	
	for item in doc[1].lower().split(' ') :
		dico[item] = dico.get((item), 0) + 1
	
	for word, count in dico.items() :
		dico2[word].append((doc[0], count))

for entry in dico2.items() :
	total = 0
	for item in entry[1] :
		total = total + item[1]
	dico2[entry[0]].append(total)

for i in sorted(dico2.items(), key = lambda x:x, reverse = False) :
	print(i)