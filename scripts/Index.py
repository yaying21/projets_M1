
import glob

import pprint

class Document(object) :

    def __init__(self,fic,lg='fr'):

        self.name = fic

        self.langue = lg

        self.content = open(fic,encoding='utf-8').read()

    def tokenized(self) :

        self.tokens = self.content.split()

    def lemmatized(self) :
        pass

    def postaggued(self) :
        pass

    def lemma_pos(self) :
        pass

class Fable(Document) :

    def __init__(self,fic,lg='fr'):

        Document.__init__(self,fic,lg)

        self.titre = self.content.split('\n')[0]


# class Corpus(object) :


class Index(object) :

    def __init__(self,docs):



        self.dic = {}
        self.empty = True
        if type(docs) != list or len(docs) <2 :
            raise ValueError("Ce n'est pas une liste ou bien elle ne contient qu'un doc")

        for doc in docs :

            if not hasattr(doc,'titre') :

               doc.titre = doc.name
            doc.tokenized()
        self.docs = docs


    def maxFreq(self,word):

        pass


    def initialize(self):

        if self.empty :

            for doc in self.docs :
                Index.indexing(self,doc,doc.tokens)
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


    def indexing(self,doc,tokens):
        if not tokens :
            self.words = [cle for cle in self.dic]
            return  0
        else :
            token = tokens[0]
            if token not in self.dic :
                self.dic[token] = {doc.titre: 1}
            else:
                if doc.titre not in self.dic[token]:
                    self.dic[token].update({doc.titre: 1})
                else:
                    self.dic[token][doc.titre] += 1
            try :
                return Index.indexing(self,doc,tokens[1:])
            except RecursionError :
                self.words = [cle for cle in self.dic]
                return 0





if __name__ == '__main__':

    fables = [Fable(doc) for doc in glob.glob('fables/*')]

    index = Index(fables)

    index.initialize()
    new_doc = Fable(glob.glob('new_doc/*.txt')[0])
    new_doc.tokenized()
    index.indexing(new_doc,new_doc.tokens)
    index.blockIndex()
    index.unBlockIndex()
    pprint.pprint(index.dic)
    max  = index.maxFreq('courage')
    # index.initialize()



