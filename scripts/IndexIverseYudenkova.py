#Kristina Yudenkova
#index_inverse_yudenkova.py -- dictionnaires
#données: trois phrases stockées dans trois variables
#résultat: un dictionnaire où les clés sont les tokens des trois phrases et les valeurs, les phrases dans lesquelles ces tokens apparaissent
        #  un dictionnaire où les clés sont les  phrases et les valeurs, le nombre d'occurrences des tokens

from collections import Counter, defaultdict

#un dictionnaire de phrases avec les mots à indexer
dico_phrases={"phrase1" : "le repas n' est pas mauvais",
              "phrase2" : "si , je le trouve pas bon",
              "phrase3" : "j' avoue il est vraiment mauvais"}
#spliter les valeurs du dictionnaire en mots
for (c, v) in dico_phrases.items():
    dico_phrases[c] = v.split()

dico_frequence=defaultdict(Counter)
for (c, v) in dico_phrases.items():
    for mot in v:
        dico_frequence[mot][c]+=1
        
for phrase in sorted(dico_frequence.items()):
    print(phrase)

print("**********************************")

#compter la frequence de chaque mot dans la phrase
dico_frequence=defaultdict(Counter)
for (c, v) in dico_phrases.items():
    for mot in v:
        dico_frequence[c][mot]+=1

for token in sorted(dico_frequence.items()):
    print(token)
