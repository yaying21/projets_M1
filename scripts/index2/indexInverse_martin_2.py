# -*- coding: utf-8 -*-
# Martin Digard

"""
ANALYSE
- lemmatisation
- tokénisation
- postagging
- stopwordisation

INDEXATION

FREQUENCE MAXIMUM
Pour un mot donné :
   - le doc où il apparaît le plus de fois.

TF-IDF (pas fini)
Pour un mot donné dans un doc donné :
     - son tf-idf.
"""

import glob
import spacy
from spacy import displacy
nlp = spacy.load('fr')
from collections import Counter, defaultdict

corpus = sorted(glob.glob('../5_corpus-test-perso/*'))
tokens = defaultdict(list)
df = Counter()
print()

for fichier in corpus :
    nom_fichier = ( fichier.replace('../5_corpus-test-perso/','') )
    with open(fichier) as document:
        contenu = document.read()
        texte = nlp(contenu)
        freq_token = Counter()
        for token in texte:
            if not ( token.is_stop or token.is_space ) :
                token = ( f"{token.lemma_} - {token.pos_}" )
                freq_token[token] += 1
        for k,v in freq_token.items():
            tf = v / len(texte)
            valeur = ( nom_fichier, v, 'tf : ' + str(tf))
            tokens[k].append(valeur)
for k,v in sorted(tokens.items()):
    print ( k + ' :\n')
    print ( f"\tIndexation : {v}")
    if ( max(v) ):
        print( f"\tFréquence maximum dans : {max(v)}")

    print()






















print()
