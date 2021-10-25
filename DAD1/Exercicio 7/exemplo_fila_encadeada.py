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

    def push(self):
        temp = Node()
        if temp:
            temp.setvalor(int(input("Entre com um valor: ")))
            temp.setprox(None)     # opcional, sem efeito
            if not self.__ini:
                self.__ini = self.__fim = temp  # primeiro nó
            else:  # a partir do segundo nó
                self.__fim.setprox(temp)
                self.__fim = temp
            Fila.printall(self)

    def pop(self):
        if self.__ini:  # excluir quaisquer elementos
            self.__ini = self.__ini.getprox()
            if not self.__ini: # foi excluído o último nó
                self.__fim = None
        Fila.printall(self)

    def printall(self):
        if self.__fim:
            temp = self.__ini
            saida = "\nFila\n"
            while temp:
                saida += str(temp.getvalor()) + '\t'
                temp = temp.getprox()
            print(saida)
        else:
            print('Fila vazia')

f = Fila()
while True:
    op = int(input('\nMenu\n1-Inserir\n2-Excluir\n3-Sair\nOpção: '))
    if op == 1:
        f.push()
    elif op == 2:
        f.pop()
    elif op == 3:
        break
    else:
        print('Op inválida')