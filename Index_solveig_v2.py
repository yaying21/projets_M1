# -*- coding: utf-8 -*-


import glob

import pprint

import spacy
from spacy import displacy
nlp = spacy.load('fr')

from collections import defaultdict, Counter

class Document(object) :

    def __init__(self,fic,lg='fr'):

        self.name = fic

        self.langue = lg

        self.content = open(fic,encoding='utf-8').read()
        
        self.nlpready = nlp(self.content)

    def tokenized(self) :
        self.tokens = []
        for token in self.nlpready:
            self.tokens.append(token.text)

    def lemmatized(self) :
        self.lemmas = []
        for token in self.nlpready:
            if token.is_stop == False and token.is_punct == False and token.is_space == False:
                self.lemmas.append(token.lemma_)

    def postaggued(self) :
        self.pos = defaultdict()
        for token in self.nlpready:
            if token.is_stop == False:
                self.pos[token.text] = token.pos_

    def lemma_pos(self) :
        self.lemmapos = defaultdict()
        for token in self.nlpready:
            if token.is_stop == False:
                self.lemmmapos[token.lemma_] = token.pos_
        
        

class Fable(Document) :

    def __init__(self,fic,lg='fr'):

        Document.__init__(self,fic,lg)

        self.titre = self.content.split('\n')[0]


# class Corpus(object) :


class Index(object) :

    def __init__(self,docs):



        self.dic = defaultdict(Counter)
        self.empty = True
        if type(docs) != list or len(docs) <2 :
            raise ValueError("Ce n'est pas une liste ou bien elle ne contient qu'un doc")

        self.nbtokens = defaultdict()
        for doc in docs :

            if not hasattr(doc,'titre') :

               doc.titre = doc.name
            doc.tokenized()
            self.nbtokens[doc.titre] = len(doc.tokens) # j'aurai besoin du nombre de mots par doc pour calculer le tf
            doc.lemmatized()
        self.docs = docs


    def maxFreq(self,word):
        for cle, valeur in self.dic.items():
            if cle == word:
                if len(self.dic[word]) == 1:
                    return(f"{cle} : {valeur}")
                else:
                    for cle, valeur in self.dic[word].most_common(1):
                        return(f"{word} : {cle}")
                


    def initialize(self):

        if self.empty :

            for doc in self.docs :
                Index.indexing(self,doc,doc.lemmas)
            self.empty = False
            # pprint.pprint(self.dic)

        else :
            raise AttributeError("L'index n'est pas vide, vous ne pouvez pas l'initialiser")

    def blockIndex(self,) :

        self.dic = {elem: [(cle, v[cle]) for cle in v] for (elem, v) in self.dic.items()}
        self.blocked = True

    def unBlockIndex(self):


        self.dic = {elem:{tup[0]:tup[1] for tup in v} for (elem, v) in self.dic.items()}
        self.blocked = False


    def indexing(self,doc,lemmas):
        if not lemmas :
            self.words = [cle for cle in self.dic]
            return  0
        else :
            lemma = lemmas[0]
            if lemma not in self.dic :
                self.dic[lemma][doc.titre] = 1
            else:
                if doc.titre not in self.dic[lemma]:
                    self.dic[lemma][doc.titre] = 1
                else:
                    self.dic[lemma][doc.titre] += 1
            try :
                return Index.indexing(self,doc,lemmas[1:])
            except RecursionError :
                self.words = [cle for cle in self.dic]
                return 0
                
    def tf_idf(self, word):
        tfidf = defaultdict(defaultdict)
        for cle, valeur in self.dic[word].items():
            tf = self.dic[word][cle]/self.nbtokens[cle]
            idf = len(self.docs)*1/len(self.dic[word])
            tfidf[word][cle] = (self.dic["courage"][cle], tf*idf)
        return tfidf





if __name__ == '__main__':

    fables = [Fable(doc) for doc in glob.glob('../fables/test_fables/*.txt')]

    index = Index(fables)

    index.initialize()

    pprint.pprint(index.dic)
    max  = index.maxFreq('courage')
    print(max)
    tfidf = index.tf_idf('courage')
    for cle, valeur in tfidf.items():
        print(cle, " :\n", valeur)
    # index.initialize()


