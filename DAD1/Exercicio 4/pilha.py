class No_pilha:

    def __init__(self):
        self.__valor = 0
        self.__proximo = None

    def getValor(self):
        return self.__valor

    def setValor(self, v):
        self.__valor = v

    def getProximo(self):
        return self.__proximo

    def setProximo(self, prox):
        self.__proximo = prox

class Pilha:

    def __init__(self):
        self.__topo = None

    def push(self):
        novo = No_pilha()
        if novo:
            novo.setValor(int(input('Entre com o valor: ')))
            if self.__topo:
                novo.setProximo(self.__topo)
            self.__topo = novo
        self.printall()

    def pop(self):
        if self.__topo:
            self.__topo = self.__topo.getProximo()
            self.printall()
        else:
            print('Pilha vazia')

    def printall(self):
        if self.__topo:
            saida = '\nPilha:\n'
            temp = self.__topo
            while temp:
                saida += str(temp.getValor()) + '\n'
                temp = temp.getProximo()
            print(saida)
        else:
            print('Pilha vazia')
    
    def printtop(self):
        if self.__topo:
            self.__topo = self.__topo.getValor()
            print("Topo =",self.__topo)
    
    def soma(self):
        if self.__topo:
            soma = 0
            cont = self.__topo
            self.__contagem = 0 
            while cont:
                soma += cont.getValor()
                cont = cont.getProximo()
                self.__contagem +=1
            return soma 
        else:
            print("Você não tem valores na lista")
    
    def media (self):
        if self.__topo:
            media = 0
            media = self.soma() / self.__contagem
            print("A media é:", media)
        else:
            print("Não temos valores na pilha")

aPilha = Pilha()
while True:
    op = int(input('1-Inserir\n2-Excluir\n3-Topo\n4-Soma\n5-Media\n6-Sair\nOpção: '))
    if op == 1:
        aPilha.push()
    elif op == 2:
        aPilha.pop()
    elif op == 3:
        aPilha.printtop()
    elif op == 4:
        print("A soma dos elementos é",aPilha.soma())   
        print("\n")
    elif op == 5:
        aPilha.media()
        print("\n")
    elif op == 6:
        break
    else:
        print('Opção inválida!')
del aPilha