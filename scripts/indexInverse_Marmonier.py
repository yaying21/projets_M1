import os
import re
from collections import Counter

# Les fichiers textes encodés au format UTF-8 doivent
# être déposés dans un repertoire dénommé "texts", au
# sein du répertoire courant:
sourcePath = "./texts/" 
texts = os.listdir(sourcePath)

class IndexInverse:
	def __init__(self, fileList):
		self.fileList = fileList
	
	def getDocDict(self):
		docDict= {}
		for file in self.fileList:
			path = sourcePath +file
			with open(path, "r") as f:
				text = f.read()
			docDict[file] = text
		return(docDict)
	
	def getIndex(self):
		documents = self.getDocDict()
		invertedIndex = {}
		for key, doc in documents.items():
			#doc = re.sub(r"([.,()-])", " \1", doc)
			doc = re.sub(r"(\.|,|\(|\)|-)", " \1 ", doc)
			doc = re.sub(r"'", r"' ", doc)
			doc = doc.lower().split()
			ind1 = Counter()
			words = []
			for word in doc:
				ind1[word] += 1
				words.append(word)
			for element in set(words):
				entry = [(key, ind1[element])]
				if element in invertedIndex.keys():
					invertedIndex[element] += entry
				else:
					invertedIndex[element] = []
					invertedIndex[element] += entry
		return invertedIndex


T = IndexInverse(texts)
##print(T.getDocDict())
##print("\n"*3)
ind = T.getIndex()
print(ind)

            
