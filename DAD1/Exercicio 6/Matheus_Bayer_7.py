class No_pilha:
    def __init__(self): 
        self.__valor = 0.0
        self.__proximo = None

    def setValor(self, v):
        self.__valor = v
  
    def setProximo(self, prox):
        self.__proximo = prox

    def getValor(self):
        return self.__valor
  
    def getProximo(self):
        return self.__proximo
    
class Pilha:
    def __init__(self):
        self.__topo = None
    
    def push(self,num):
        novo = No_pilha()
        if novo:
            novo.setValor(num)
            if self.__topo:
                novo.setProximo(self.__topo)
            self.__topo = novo

    def printall(self):
        if self.__topo:
            saida = '\n===Binario===\n'
            temp = self.__topo
            while temp:
                saida += (f"{str(temp.getValor())}")
                temp = temp.getProximo()
            print(saida)
        else:
            print('Pilha vazia')
#########################################################################
def main():
    numero = Pilha()
    while True:
        op = int(input("Opções:\n"
                "1-Decimal para binario\n"
                "2-Binario para decimal\n"
                "3- encerra\n"
                "opção:"))
        
        if op == 1:
            print("Digite o numero para saber o binario dele:")
            print("Lembrando que este numero precisa ser positivo")
            while True:
                num=(int(input("Digite o numero:")))
                if num > 0:
                    numero.push(num)
                    while True:
                        div = num 
                        resto = Pilha()
                        while div > 0:
                            Div = int(div / 2)
                            resto.push(int(div % 2))                  
                            div = Div #6,3,1
                        break
                    resto.printall()
                    break
                else:
                    print("Numero digitado é nagativo")
        elif op ==2:
            while True:
                num = int(input("Digite o numero binario para saber o decimal dele:"))
                Binario = 0
                b = str(num)
                if num > 0:
                    numero.push(num)
                    for numer in range(len(b)):
                        Binario += numer ** 2
                        print (numer)
                break
            print(f"Binario:{Binario}")


        elif op == 3:
            break
        else:
            print("Digite uma opção valida")
   

if __name__ == '__main__':
    main()