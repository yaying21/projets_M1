
import glob

import pprint

import spacy

import math

nlp=spacy.load('fr_core_news_sm')

class Document(object) :

    def __init__(self,fic,lg='fr'):

        self.name = fic

        self.langue = lg

        self.content = open(fic,encoding='utf-8').read()

        self.nlpcontent = nlp(self.content)
    def stopwordise(self) :
        self.stopwords = [token for token in self.nlpcontent if (token.is_stop==False and token.is_punct==False and token.is_space==False)]

    def tokenized(self, stopword=False) :
        if stopword==True :
            if not hasattr(self,'stopword'):
                self.stopwordise()
            self.tokens = [token.text for token in self.stopwords]
        else:
            self.tokens = [token.text for token in self.nlpcontent]

    def lemmatized(self, stopword=False) :
        if stopword==True :
            if not hasattr(self,'stopword'):
                self.stopwordise()
            self.lemmas = [token.lemma_ for token in self.stopwords]
        else:
            self.lemmas = [token.lemma_ for token in self.nlpcontent]

    def postaggued(self, stopword=False) :
        if stopword==True :
            if not hasattr(self,'stopword'):
                self.stopwordise()
            self.pos = [(token.text,token.pos_)for token in self.stopwords]
        else:
            self.pos = [(token.text,token.pos_) for token in self.nlpcontent]

    def lemma_pos(self, stopword=False) :
        if stopword==True :
            if not hasattr(self,'stopword'):
                self.stopwordise()
            self.lemma_pos = [(token.text,token.pos_)for token in self.stopwords]
        else:
            self.lemma_pos = [(token.lemma_,token.pos_) for token in self.nlpcontent]



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
            doc.lemmatized()
        self.docs = docs


    def maxFreq(self,word):

        fq_base={doc:valeur[0] for doc,valeur in self.dic[word].items()}
        max_key=max(fq_base, key=fq_base.get)
        return max_key


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


    def indexing(self,doc,tokens):
        if not tokens :
            self.words = [cle for cle in self.dic]
            return  0
        else :
            token = tokens[0]
            if token not in self.dic :
                self.dic[token] = {doc.titre: [1]}
            else:
                if doc.titre not in self.dic[token]:
                    self.dic[token].update({doc.titre: [1]})
                else:
                    self.dic[token][doc.titre][0] += 1
            try :
                return Index.indexing(self,doc,tokens[1:])
            except RecursionError :
                self.words = [cle for cle in self.dic]
                return 0
    def tf_idf_ation(self, word, doc_titre):
        doc=next((doc for doc in self.docs if doc.titre == doc_titre), None)
        nb_token=len(doc.tokens)
        tf=self.dic[word][doc_titre][0]/nb_token
        idf=math.log2(len(self.docs)/len(self.dic[word]))
        tfidf=(tf*idf)
        self.dic[word][doc_titre].append(tfidf)
        return tfidf





if __name__ == '__main__':

    fables = [Fable(doc) for doc in glob.glob('../fables/test_fables/*.txt')]


    index = Index(fables)

    index.initialize()
    #new_doc = Fable(glob.glob('new_doc/*.txt')[0])
    #new_doc.tokenized()
    #index.indexing(new_doc,new_doc.tokens)
    index.blockIndex()
    index.unBlockIndex()
    print(index.dic["bon"])

    print(index.maxFreq('beau'))
    print(index.tf_idf_ation('buste','Le Renard et le Buste'))
    #print(index.tf_idf_ation('beau','doc1.txt'))
    #pprint.pprint(index.dic)
