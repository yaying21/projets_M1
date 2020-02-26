import os
import re
import math
from collections import Counter
import spacy

nlp = spacy.load('fr_core_news_sm')

sourcePath = "./test_fables/"
texts = os.listdir(sourcePath)

class IndexInverse:
    def __init__(self, fileList):
        self.fileList = fileList

    def getDocDict(self):
        docDict = {}
        for file in self.fileList:
            path = sourcePath + file
            with open(path, "r") as f:
                text = f.read()
            docDict[file] = text
        return(docDict)
    
    def getIndexTFIDF(self):
        stopWordsFR = ['alors', 'au', 'aucuns', 'aussi', 'autre', \
         'avant', 'avec', 'avoir', 'bon', 'car', 'ce', \
         'cela', 'ces', 'ceux', 'chaque', 'ci', 'comme', \
         'comment', 'dans', 'des', 'du', 'dedans', 'dehors', \
         'depuis', 'devrait', 'doit', 'donc', 'dos', 'début', \
         'elle', 'elles', 'en', 'encore', 'essai', 'est', 'et', \
         'eu', 'fait', 'faites', 'fois', 'font', 'hors', 'ici', \
         'il', 'ils', 'je', 'juste', 'la', 'le', 'les', 'leur', \
         'là', 'ma', 'maintenant', 'mais', 'mes', 'mien', 'moins', \
         'mon', 'mot', 'même', 'ni', 'nommés', 'notre', 'nous', \
         'ou', 'où', 'par', 'parce', 'pas', 'peut', 'peu', 'plupart', \
         'pour', 'pourquoi', 'quand', 'que', 'quel', 'quelle', \
         'quelles', 'quels', 'qui', 'sa', 'sans', 'ses', \
         'seulement', 'si', 'sien', 'son', 'sont', 'sous', \
         'soyez', 'sujet', 'sur', 'ta', 'tandis', 'tellement', \
         'tels', 'tes', 'ton', 'tous', 'tout', 'trop', 'très', \
         'tu', 'voient', 'vont', 'votre', 'vous', 'vu', 'ça', \
         'étaient', 'état', 'étions', 'été', 'être']
        documents = self.getDocDict()
        invertedIndex = {}
        for key, doc in documents.items():
            bufferIndex = Counter()
            tokDoc = nlp(doc)
            lemmas = []
            for token in tokDoc:
                if token.text.lower not in stopWordsFR:
                    bufferIndex[token.lemma_] += 1
                    lemmas.append(token.lemma_)
            for element in set(lemmas):
                tf = bufferIndex[element]/len(tokDoc)
                entry = [[key, bufferIndex[element], tf]]
                if element in invertedIndex.keys():
                    invertedIndex[element] += entry
                else:
                    invertedIndex[element] = []
                    invertedIndex[element] += entry
        for key, value in invertedIndex.items():
            for element in value:
                [x, y, z] = element
                idf = math.log(len(self.fileList)/len(value))
                element[2] = z * idf
        return invertedIndex
    
    def maxFreq(self):
        invIndex = self.getIndex()
        maxFreqIndex = {}
        for key, value in invIndex.items():
            maxOcc = 0
            for element in value:
                (x, y) = element
                if (y > maxOcc):
                    maxOcc = y
                    maxDoc = x
            maxFreqIndex[key] = (maxDoc, maxOcc)
        return maxFreqIndex
                    

T = IndexInverse(texts)
##mfi = T.maxFreq()
##print(mfi)
indTFIDF = T.getIndexTFIDF()
print(indTFIDF)


    


                

            

            
            
            

