# Xinyi Shen
from collections import Counter,defaultdict


docs = {"doc1": "la bouffe est pas mauvaise", "doc2": "si je le trouve pas bon", "doc3": "j'avoue il est vraiment mauvais"}

dic=defaultdict(list)
for doc, phrase in docs.items():
	cnt=Counter()
	for token in phrase.split():
		cnt[token] +=1
	for token, item in cnt.items():
		valeur=(doc, item)
		dic[token].append(valeur)
		
print(dic)

