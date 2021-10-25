class No_pilha:

    def __init__(self):
        self.__valor = 0
        self.__proximo = None
        self.__Nome = " "
        self.__idade = 0

    def getValor(self):
        return self.__valor

    def setValor(self, v):
        self.__valor = v

    def getProximo(self):
        return self.__proximo

    def setProximo(self, prox):
        self.__proximo = prox

    def setNome(self,n):
        self.__Nome = n

    def getNome(self):
        return self.__Nome
    
    def setIdade(self,i):
        self.__idade = i
    
    def getIdade(self):
        return self.__idade

class Pilha:

    def __init__(self):
        self.__topo = None

    def push(self):
        novo = No_pilha()
        if novo:
            novo.setValor(int(input('Entre com o valor: ')))
            novo.setNome(input("Digite o Nome do aluno:"))
            novo.setIdade(int(input("Digite a idade do aluno:")))
            if self.__topo:
                novo.setProximo(self.__topo)
            self.__topo = novo
        print('\n')
        self.printall()

    def pop(self):
        if self.__topo:
            self.__topo = self.__topo.getProximo()
            self.printall()
        else:
            print('Pilha vazia')

    def printall(self):
        if self.__topo:
            saida = '\n===Pilha===\n'
            temp = self.__topo
            while temp:
                saida += (f"     {str(temp.getValor())}\n"
                          f"Nome: {temp.getNome()}\n"
                          f"Idade:{temp.getIdade()}\n")
                temp = temp.getProximo()
            print(saida)
        else:
            print('Pilha vazia')
    
    def printtop(self):
        if self.__topo:
            temp = self.__topo
            print("===Topo===\n"
                  f"     {temp.getValor()}\n"
                  f"{temp.getNome()}\n"
                  f"{temp.getIdade()}\n")
    
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
##############################################################################################################################################
aPilha = Pilha()
while True:
    op = int(input('1-Inserir\n2-Excluir\n3-Topo\n4-Media\n5-Sair\nOpção: '))
    if op == 1:
        print('\n')
        aPilha.push()
    elif op == 2:
        print('\n')
        aPilha.pop()
    elif op == 3:
        print('\n')
        aPilha.printtop()
    elif op == 4:
        print('\n')
        aPilha.media()
        print("\n")
    elif op == 5:
        break
    else:
        print('Opção inválida!')
del aPilha