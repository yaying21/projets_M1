
import glob

import pprint

import sys

class Document(object) :

    def __init__(self,fic,lg='fr'):

        self.name = fic

        self.langue = lg
        print(fic)

        self.content = open(fic,'r').read()

    def tokenized(self) :

        self.tokens = self.content.split()

    def lemmatized(self) :
        pass

    def postaggued(self) :
        pass

class Fable(Document) :

    def __init__(self,fic,lg='fr'):

        Document.__init__(self,fic,lg)

        self.titre = self.content.split('\n')[0]


# class Corpus(object) :
# coding : utf-8

class Index(object) :

    def __init__(self,docs):


        self.dic = {}
        self.empty = True
        if type(docs) != list or len(docs) <2 :
            raise ValueError("Ce n'est pas une liste !!")

        for doc in docs :

            if not hasattr(doc,'titre') :

               doc.titre = doc.name
            doc.tokenized()
        self.docs = docs

    def initialize(self):

        if self.empty :

            for doc in self.docs :
                tokens = doc.tokens
                self.indexing(doc,tokens)
            pprint.pprint(self.dic)
            self.empty = False
        else :
            raise AttributeError("L'index n'est pas vide, vous ne pouvez pas l'initialiser")
            
    def indexing(self,doc,tokens) :
        if not tokens :
            return 0

        else :
            token = tokens[0]
            if token not in self.dic :
                self.dic[token] = [{doc.titre:1}]
            elif token in self.dic and doc.titre not in self.dic[token] :
                self.dic[token].append({doc.titre:1})
            else :
                self.dic[token][doc.titre] += 1
            try :
                return self.indexing(doc,tokens[1:])
            except RuntimeError :
                return 0










if __name__ == '__main__':

    fables = [Fable(doc) for doc in glob.glob('../fables/train_fables/*.txt')]

    index = Index(fables)

    index.initialize()
    
    new_doc = Fable('../README.md')
    new_doc.tokenized()
    tokens = new_doc.tokens
    index.indexing(new_doc,tokens)


