# -*- coding: utf-8 -*-
# Martin Digard

'''
À PARTIR DES 3 PHRASES.
'''

from collections import Counter, defaultdict

doc1 = "le repas n’est pas mauvais"
doc2 = "si, je le trouve pas bon"
doc3 = "J'avoue il est vraiment mauvais"

documents = [doc1,doc2,doc3]
tokens = defaultdict(list)
for phrase in documents:
    freq_token = Counter()
    for token in phrase.split():
        freq_token[token] += 1
    for k,v in freq_token.items():
        valeur = (phrase, v)
        tokens[k].append(valeur)
print()
for e in sorted(tokens.items()):
    print(e)
print()
