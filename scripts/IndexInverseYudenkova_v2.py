#Yudenkova Kristina
#Calcule le tf d'un token
from collections import Counter, defaultdict
import spacy
nlp=spacy.load('fr_core_news_sm')
from spacy.lang.fr.stop_words import STOP_WORDS

docs={"doc1" : "Le climat océanique avec des hivers assez doux et des étés relativement frais", "doc2" : "Les   précipitations   sont   abondantes   toute   l’année   dans   l’ouest   de   la   France"}
dico=defaultdict(list)
for c, v in docs.items():
    for mot in v.split():
        my=nlp(mot)
        for word in my:
            if word.is_stop == False:
                if word not in dico:
                    dico[c].append(word.lemma_)
dico2=defaultdict(list)
cnt = defaultdict(Counter)
for cle, valeur in dico.items():
    for item in valeur:
        cnt[cle][item] += 1
for cle, val in cnt.items():
    for item in val:
        m=cnt[cle][item]/len(val)
        dico2[item].append((cle,m))
print(dico2)
