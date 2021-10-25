class No_pilha:

    def __init__(self):
        self.__valor = 0
        self.__proximo = None   #nó anterior

    def getValor(self):
        return self.__valor

    def setValor(self):
        self.__valor = int(input('Digite um numero para entrar na pilha: '))

    def getProximo(self):
        return self.__proximo

    def setProximo(self, prox):
        self.__proximo = prox

class Pilha:

    def __init__(self):
        self.__topo = None

# Pilha(    novo[__valor:1] ,  novo2[__valor:2, __setproximo : novo], novo3[__valor:3,__proximo: novo2])
# self__topo = novo3

    def push(self):
        novo = No_pilha()           

        if novo:
            novo.setValor()
            if self.__topo:
                novo.setProximo(self.__topo) 
            self.__topo = novo
        

    def pop(self):
        if self.__topo:     
            self.__topo = self.__topo.getProximo()
            
        else:
            print('Pilha vazia')

    def printall(self):
        if self.__topo:          
            temp = self.__topo
            while temp:
                print(temp.getValor())               
                temp = temp.getProximo()
            
    
    def printtop(self):
        if self.__topo:
            self.__topo = self.__topo.getValor()
            return self.__topo

    def returntop(self):
        return self.__topo.getValor()
    

    

#####################################################################################################
class Node:

    def __init__(self):
        self.__valor = 0
        self.__prox = None

    def getvalor(self):
        return self.__valor

    def setvalor(self, v):
        self.__valor = v

    def getprox(self):
        return self.__prox

    def setprox(self, p):
        self.__prox = p

class Fila:

    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push(self,n):
        temp = Node()
        if temp:
            temp.setvalor(int(n))
            temp.setprox(None)     # opcional, sem efeito
            if not self.__ini:
                self.__ini = self.__fim = temp  # primeiro nó
            else:  # a partir do segundo nó
                self.__fim.setprox(temp)
                self.__fim = temp
            

    def pop(self):
        if self.__ini:  # excluir quaisquer elementos
            self.__ini = self.__ini.getprox()
            if not self.__ini: # foi excluído o último nó
                self.__fim = None
        

    def printall(self):
        if self.__fim:
            temp = self.__ini
            
            while temp:
                print(temp.getvalor())
                temp = temp.getprox()               
        else:
            print('Fila vazia')


aPilha = Pilha()
aFila = Fila()
bFila = Fila()
cont = 0
num = 0

while True:

    aPilha.push()

    if aPilha.returntop() == 0  :
        aPilha.pop()
        break

    if aPilha.returntop() %2 == 0:
        aFila.push(aPilha.returntop())
        
    else:
        bFila.push(aPilha.returntop())
    
print("A pilha digitada:")
aPilha.printall()

print("A Fila par")
aFila.printall()

print("A Fila impar")
bFila.printall()