# O PROBLEMA DE JOSEPHUS: 
# Examina-se um problema que pode ser solucionado de maneira simples usando uma fila 
# encadeada circular. Ele é conhecido como problema de Josephus e postula um grupo de 
# soldados circundado por uma força inimiga esmagadora. Não há esperanças de vitória sem a 
# chegada de reforços, mas existe somente um cavalo disponível para escapar. Os soldados 
# entram num acordo para determinar qual deles deverá escapar e trazer ajuda. Eles formam um 
# círculo e um número n é fornecido. Um de seus nomes é fornecido também. Começando pelo 
# soldado cujo nome foi fornecido, eles começam a contar ao longo do círculo no sentido 
# permitido por uma estrutura fila. Quando a contagem alcança n, esse soldado é retirado do 
# círculo, e a contagem reinicia com o soldado seguinte. O processo continua de maneira que, 
# toda vez que n é alcançado, outro soldado sai do círculo. Todo soldado retirado do círculo não 
# entra mais na contagem. O último soldado que restar deverá montar no cavalo e escapar.
# Considerando um número n, a ordem dos soldados no círculo e o soldado a partir do qual 
# começa a contagem, o problema consiste em determinar a sequência na qual os soldados são 
# eliminados do círculo e identificar o soldado que escapará.

# A entrada para o programa é o nome dos soldados, que será o sequenciamento do círculo, 
# começando pelo soldado a partir do qual a contagem deve ser iniciada. Ao final, o programa 
# deve imprimir os nomes na sequência em que são eliminados e o nome do soldado que 
# escapará.
# Por exemplo, suponha que n = 3, o soldado a partir do qual começa a contagem seja o A, e que 
# existam cinco soldados, chamados A, B, C, D e E. Contamos três soldados a partir de A para 
# que C seja eliminado primeiro. Em seguida, começamos em D e contamos D, E e novamente A 
# para que A seja eliminado a seguir. Depois, contamos B, D e E (C já foi eliminado) e, 
# finalmente, B, D e B, de modo que D seja o soldado a escapar.
# Uma fila encadeada circular, na qual cada nó representa um soldado, é uma estrutura de dados 
# natural para usar na solução deste problema. É possível alcançar qualquer nó a partir de 
# qualquer outro, percorrendo o círculo. Para representar a remoção de um soldado do círculo, 
# um nó é eliminado da fila circular. Por último, quando só restar um nó na lista, o resultado será 
# determinado.

from random import randint

class Node():
    __nome = None
    __proximo = None
    __numero = None

    def __init__(self):

        self.__nome = None
        self.__proximo = None
        self.__numero = None

    def getnome(self):
        return self.__nome

    def setnome(self, nome):
        self.__nome = nome

    def getproximo(self):
        return self.__proximo

    def setproximo(self, proximo):
        self.__proximo = proximo

    def getnumero(self):
        return self.__numero
    
    def setnumero(self, numero):
        self.__numero = numero

class Fila:
    __num = None

    def __init__(self):
        self.__final = None
        self.__num = 0

    def push(self,nome):
        temp = Node()
        if temp:
            self.__num = self.__num + 1
            print(self.__num)
            temp.setnome(nome)
            temp.setnumero(self.__num)

            if self.__final:                  
                temp.setproximo(self.__final.getproximo())                  
                self.__final.setproximo(temp)   
                self.__final = temp               
            else:                 
                temp.setproximo(temp)                  
                self.__final = temp        
            self.print_all()         
        else:               
            print("Ocorreu um erro")    
        
    def pop(self):        
        if self.__final:  
            nome = self.__final.getproximo().getnome()     

            if (self.__final.getproximo() == self.__final):                
                self.__final = None
            else:
                proximo = self.__final.getproximo().getproximo()
                self.__final.setproximo(proximo)
            print("Nome removido: ", nome,"\n")
            
        else:
            print("Fila vazia")

    def print_all(self):
        if self.__final:       
            temp = Node()
            temp = self.__final.getproximo()
            saida = " \nFila circular:\n"  
            while temp != self.__final:   
                saida +=(f"\tNome:{temp.getnome()}\n")   
                temp = temp.getproximo()         
            print(saida,
                 f"\tNome:{temp.getnome()}\n")      
        else:
            print("Fila vazia")

    def sortear(self):
        
        n = randint(1,self.__num)

        if self.__final:
            temp = Node()
            temp = self.__final.getproximo()
            aux = self.__final
            while temp != aux:
                if n == temp.getnumero():
                    print(f'{temp.getnome()} foi morto!')
                    self.pop()
                    break
                temp = temp.getproximo() 

            if n == temp.getnumero():
                    print(f'{temp.getnome()} foi morto!')
                    self.pop()
                                       

def main():
  op = 0 
  lista = Fila()

  while True:
    op = int(input("Opções:\n"
                   "1 - Cadastrar soldado.\n"
                   '2 - Teste automatizado\n'
                   '3 - PrintAll\n'
                   '4 - Sortear\n'
                   "5 - Sair.\n"
                   "Informe opção: \n"))
    
    if op == 1:
      soldado = input("Informe o nome do soldado:\n")
      lista.push(soldado)
    
    elif op == 2:
      lista.push(3, "Carlos")
      lista.push(2, "Bruno")
      lista.push(1, "Ana")
      lista.push(4, "Diego")
      lista.push(6, "Fernando")
      lista.push(5, "Edna")
    
    elif op == 3:
        lista.print_all()

    elif op == 4:
        lista.sortear()

    elif op == 5:
      break

    else:
      print("Opção inválida.")

if __name__ == '__main__':
  main()
