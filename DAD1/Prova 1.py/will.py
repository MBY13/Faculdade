class No_pilha:
    def __init__(self): 
        self.__proximo = None
        self.__CEP = ''
        self.__Numero = 0
        self.__Complemento = ''

    def setProximo(self, prox):
        self.__proximo = prox
    def getProximo(self):
        return self.__proximo

    def  setCEP(self ,cep):
        self.__CEP = cep
    def  getCEP(self):
        return self.__CEP

    def setNumero(self,numero):
        self.__Numero = numero
    def getNumero(self):
        return self.__Numero

    def setComplemento(self , complemento):
        self.__Complemento = complemento
    def getComplemento(self):
        return self.__Complemento

    def toString(self):
        Str = (self.__CEP + '' + self.__Numero + '' + self.__Complemento)
        return Str
    
class Pilha:
    def __init__(self):
        self.__topo = None
    
    def push(self):
        novo = No_pilha()
        if novo:
            novo.setCEP(input('Digite o CEP: '))
            novo.setNumero(input('Digite o numero: '))
            novo.setComplemento(input('Digite o complemento: '))
            if self.__topo:
                novo.setProximo(self.__topo)
            self.__topo = novo
            self.printall()

    def pop(self):
        
        if self.__topo:
            self.__topo = self.__topo.getProximo()
        else:
            print('Pilha vazia')

    def printall(self):

        if self.__topo:
            saida = '\n===Endereço===\n'
            temp = self.__topo
            while temp:
                saida += temp.toString()
                temp = temp.getProximo()
            print(saida)
        else:
            print('Pilha vazia')
    
def main():

    while True:

        pilha = Pilha()

        op = int(input(f'1) função para inserir os dados referente o endereço de um aluno;\n' 
        '2) função para remover um item cadastrado;\n' 
        '3) função para imprimir todos os endereços cadastrados.\n'
        '4 - Sair\n'))
        
        if op == 1:
            pilha.push()
        if op == 2:
            pilha.pop()
        if op == 3:
            pilha.printall()
        if op == 4:
            break
        

if __name__ == '__main__':
    main()