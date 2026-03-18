import random

class Model(object):
    def __init__(self):
        self._nMax=100
        self._tMax=6
        self._segreto=None  # lo instanzio in un altro momento, perchè io posso iniziare subito una nuova partita
        self._t=self._tMax  # se non ha ancora iniziato ha il numero massimo di tentativi


    def reset(self):
        self._segreto=random.randint(1,self._nMax)
        self._t=self._tMax
        print(f"Il numero segreto è {self._segreto}")

    def play(self,tentativo):
        self._t-=1
        if tentativo==self._segreto:  #ho vinto
            return 0            #i return li decido io
        if self._t==0:  #ho finito i tentativi
            return 2
        if tentativo>self._segreto:
            return -1
        else:
            return 1


    @property
    def nMax(self):
        return self._nMax

    @property
    def tMax(self):
        return self._tMax

    @property
    def t(self):
        return self._t



if __name__=="__main__":
    model=Model()
    model.reset()
    print(model.play(10))
    print(model.play(52))
    print(model.play(78))
    print(model.play(7))
    print(model.play(25))
    print(model.play(95))




