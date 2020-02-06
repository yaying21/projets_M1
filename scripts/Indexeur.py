
import nltk
from Evaluation import Evaluation
class Indexeur(object):

    def __init__(self,tool):

        self.tool = tool

    def requetage(self,text,requete):

        if eval(requete) :
            return '0'
        else :
            return '1'


if __name__ == '__main__':
    ind = Indexeur(nltk)
    text = "c'est vraiment pas mauvais hein"
    text2 = "franchement c'est éclaté"
    text3 = "ouais je suis d'accord la sauce est vraiment mauvaise"
    pred = []
    ref = ['1','1','0']
    pred.append(ind.requetage(text,requete = " 'mauvais' in text"))
    pred.append(ind.requetage(text2,requete=" 'mauvais' in text"))
    pred.append(ind.requetage(text3,requete=" 'mauvais' in text"))
    print(pred)
    eval = Evaluation(ref,pred)
    print(eval.f_mesure())


