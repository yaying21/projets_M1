# -*- coding: utf-8 -*-
"""
author : Mei GAN

#dictionnaire, index inversé
"""
'''
le script doit être mis dans le même répertoir que les fichiers .txt à traiter

'''
import os

corpus = {}

def get_dic(corpus, file_name, liste):
    for mot in liste:
        if mot not in corpus.keys():
            corpus[mot]=[(file_name,1)]
        else:
            exist=False
            for cal in corpus[mot]:
                if file_name == cal[0]:
                    nb = cal[1]+1
                    corpus[mot].remove(cal)
                    corpus[mot].append((file_name,nb))
                    exist=True
                    break
            if not exist:
                corpus[mot].append((file_name,1))

#lire le répertoire du script
path_file= os.getcwd()
files= os.listdir(path_file)

#lire les fichiers dans le répertore
for file in files:
    if '.txt' in file:
        words_liste = []
        file_name = os.path.join(path_file, file)
        with open(file_name, 'r') as raw_texte:
            for line in raw_texte:
                line = line.strip().split(" ")
                words_liste.extend(line)
                
            get_dic(corpus, file_name, words_liste)

print(corpus)
            



