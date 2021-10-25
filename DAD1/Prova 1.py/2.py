class No_pilha:
    def __init__(self): 
        self.__proximo = None
        self.__Nome = " "
        self.__Cep = " "
        self.__Numero = 0
        self.__Complemento = " "

    def setProximo(self, prox):
        self.__proximo = prox
    def getProximo(self):
        return self.__proximo

    def setNome(self , n):
        self.__Nome = n
    def getNome(self):
        return self.__Nome

    def  setCep(self ,c):
        self.__Cep = c
    def  getCep(self):
        return self.__Cep

    def setNumero(self,num):
        self.__Numero = num
    def getNumero(self):
        return self.__Numero

    def setComplemento(self , com):
        self.__Complemento = com
    def getComplemento(self):
        return self.__Complemento

class Pilha:

    def __init__(self):
        self.__topo = None
    
    def push(self):
        novo = No_pilha()
        if novo:
            novo.setNome(input("Digite o Nome do aluno:"))
            novo.setCep(input("Digite o CEP do aluno:"))
            novo.setNumero(int(input("Digite o numero da casa do aluno:")))
            novo.setComplemento(input("Digite o complemento:"))
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
            saida = '\n===Pilha===\n'
            temp = self.__topo
            while temp:
                saida += (f"Nome:{(temp.getNome())}\n"
                          f"CEP:{temp.getCep()}\n"
                          f"Numero:{temp.getNumero()}\n"
                          f"Complemento:{temp.getComplemento()}\n\n")
                temp = temp.getProximo()
            print(saida)
        else:
            print('Pilha vazia')

def main():
    Aluno = Pilha()

    while True:
        op = int(input("Opção\n"
                   "1 - Dados do aluno\n"
                   "2 - Remover dados anterior\n"
                   "3 - Imprime tudo\n"
                   "4 - Sair\n"
                   "Digite a opção:"))
        if op == 1:
            Aluno.push()
        elif op == 2:
            Aluno.pop()
        elif op == 3:
            Aluno.printall()
        elif op == 4:
            print("O programa encerrou!")
            break
        else:
            print("Opção Invalida")

if __name__ == "__main__":
    main()