#utf-8
#Modules.
import os, spacy, math
from collections import defaultdict
from os import listdir
sp = spacy.load("fr_core_news_sm")

#Lecture et structuration des fichiers.
stopwordslist = ["\n", "\t", "\r", "...", ".", ",", "!", "?", ":",";", "'", '"', "(", ")", "alors", "au", "aucuns", "aussi", "autre", "avant", "avec", "avoir", "bon", "car", "ce", "cela", "ces", "ceux", "chaque", "ci", "comme", "comment", "dans", "des", "du", "dedans", "dehors", "depuis", "devoir", "donc", "dos", "début", "elle", "en", "encore", "essai", "être", "et", "eu", "fois", "hors", "ici", "il", "je", "juste", "la", "le", "leur", "là", "ma", "maintenant", "mais", "mes", "mien", "moins", "mon", "mot", "même", "ni", "ne", "notre", "nous", "ou", "où", "par", "parce", "pas", "peut-être", "peu", "plupart", "pour", "pourquoi", "quand", "que", "quel", "quelle", "qui", "sa", "sans", "ses", "seulement", "si", "sien", "son", "sous", "sujet", "sur", "ta", "tandis", "tellement", "tels", "tes", "ton", "tous", "tout", "trop", "très", "tu", "votre", "vous", "vu", "ça"]

sentences = [(fichier, open(f"../fables/test_fables/{fichier}").read()) for fichier in os.listdir("../fables/test_fables")]

dico2 = defaultdict(list)
totalword = []


#Traitement des fichiers.
for doc in sentences :
	dico = {}
	normalized = []
	
	for word in (sp(doc[1])) :
		if  str(word.lemma_).lower() not in stopwordslist and len(word) < 26 :
			normalized.append(f"{word.lemma_.lower()}/{word.pos_}")
			
	totalword.append((doc[0],len(normalized)))
	
	for item in normalized :
		dico[item] = dico.get((item), 0) + 1 

	for word, count in dico.items() :
		dico2[word].append((doc[0], count))


#tf = frequ(m) dans d / nbr total de mots dans d
#idf = log2(nombre de docs dans c * ( nbr de docs où m apparaît))

#Opérations sur le dictionnaire.
dico_tfidf = {}

for entry in dico2.items() :
	total = 0
	maxfreq = 0
	docnumber = 0
	tfidf = []

	for item in entry[1] :
		docnumber = docnumber + 1
		
	for item in entry[1] :
		total = total + item[1]
		if maxfreq < item[1] :
			maxfreq = item[1]
			maxfreqdoc = item[0]
		elif (maxfreq == item[1]) :
			maxfreqdoc += f"/{item[0]}"
		for document in totalword :
			if (item[0] == document[0]):
				tf_idf = round((item[1] / document[1])*(math.log2(len(sentences)*(docnumber))),3)
				tfidf.append((item[0],tf_idf))
				break
	
	dico2[entry[0]].append(("TFIDF:", tfidf))
	
	#optionel
	dico2[entry[0]].append(f"Total:{total}")
	#optionel
	dico2[entry[0]].append(f"Maxfreq:{maxfreqdoc}")
	#optionel
	dico2[entry[0]].append(f"Nombredoc:{docnumber}")
	
#Sortie des données.
for i in sorted(dico2.items(), key = lambda x:x[0], reverse = False) :
	print(i)
