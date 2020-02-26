from glob import glob
import os
from Evaluation import Evaluation

predicted = []
expected = []


def getFile(fic,pol): 
    x = 0
    for f in glob(fic+'/*') : 
        x += 1
        os.system(f'mv {f} {pol}/')
        if x == 500 : 

            break


def predict(content) : 
    if 'good' in content : 
        return 'pos' 
    else :
        return 'neg'


def getcontentlabel(file) :
    
    expect = '' 
    if 'pos' in file : 
        expect = 'pos'
    else : 
        expect = 'neg'

    return open(file).read(),expect


def prediction(predict,file,expect) : 

    pred = predict(file)
    predicted.append(pred)
    expected.append(expect)


if __name__ == '__main__':
    os.system('pwd')

    for fic in glob('../corpus/imdb/*/*.txt') : 
        print(fic)
        file, label = getcontentlabel(fic)
        print(file)
        print(label)

        prediction(predict,file,label)
    print(predicted)
    print(expected)


    eval = Evaluation(expected,predicted)
    print(eval.getVraisPos())
    print(eval.getFauxNeg())
    print(eval.getFauxPos())
    print(eval.f_mesure())