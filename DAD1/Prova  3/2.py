class Node:
    def __init__(self):
        self.__info = 0
        self.__dir = self.__esq = None
    def getInfo(self):
        return self.__info
    def setInfo(self, info):
        self.__info = info
    def getDir(self):
        return self.__dir
    def setDir(self, dir):
     self.__dir = dir
    def getEsq(self):
        return self.__esq
    def setEsq(self, esq):
        self.__esq = esq

class Arvore():

    def inserir (self, aux, n):
        if aux is None:
            aux = Node()
            aux.setInfo(n)
        elif n < aux.getInfo():
            aux.setEsq(self.inserir (aux.getEsq(), n))
        else:
            aux.setDir(self.inserir (aux.getDir(), n))
        return aux


    def contar_no (self, raiz):
        if not raiz:
            return 0
        else:
            return 1 + self.contar_no (raiz.getEsq()) + self.contar_no (raiz.getDir())

raiz = None
arv = Arvore()
while True:
    n = int(input("Digite o Elemento(tecle 0 para parar): "))
    if n is not 0:
        raiz = arv.inserir(raiz, n)
    else:
        break
print(arv.contar_no(raiz))

