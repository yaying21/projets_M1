
from random import randint

class Des(object) :
    def __init__(self,genre):

        self.__genre = genre
        if self.__genre == 6 :
            self.__faces = [1,2,3,4,5,6]

    def getFaces(self):
        return self.__faces

    def getGenre(self):
        return self.__genre

    def jetDe(self):
        return randint(1,6)
if __name__ == '__main__':

    de1 = Des(6)
    de2 = Des(6)
    x = 0
    for i in range(100) :
        iteration = 1

        while True :

            lancer1 = de1.jetDe()
            lancer2 = de2.jetDe()
            if lancer2 != lancer1 :
                iteration += 1
            else :
                x += iteration
                print("c'est une paire de {} obtenue au {}e lancer".format(lancer1,iteration))
                break
    print("En moyenne, sur 10 tentatives, il faut {} lancers pour avoir une paire".format(x/100))