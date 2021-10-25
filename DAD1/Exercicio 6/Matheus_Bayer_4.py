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

    def push(self,nota):
        novo = No_pilha()
        if novo:
            novo.setValor(nota)
            if self.__topo:
                novo.setProximo(self.__topo)
            self.__topo = novo

    def pop(self):
        if self.__topo:
            self.__topo = self.__topo.getProximo()
        else:
            print("Pilha está vazia!")
    
    def printall(self):
        if self.__topo:
            saida = '\n===Pilha===\n'
            temp = self.__topo
            while temp:
                saida += (f"Nota:{str(temp.getValor())}\n")
                temp = temp.getProximo()
            print(saida)
        else:
            print('Pilha vazia')

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
    
    def getTopo(self):
        return self.__topo

###############################################################################################################################################
def main():
    pilha1 = Pilha() #meninos
    pilha2 = Pilha() #meninas
    while True:
        op = int(input("\nOpções:\n"
                 "1-Entrar com notas\n"
                 "2-Excluir notas\n"
                 "3-Media\n"
                 "4-Imprimir Pilhas\n"
                 "5-sair\n"
                 "Opção:"))
        if op == 1:
            while True:
                op2 = int(input ("\nOpções:\n"
                                "1-Nota Meninos\n"
                                "2-Nota Meninas\n"
                                "3-Voltar\n"
                                "Opção:"))
                if op2 == 1:
                    while True:
                        nota =(float(input("\nDigite a nota:")))
                        if nota >= 0 and nota <= 10:
                            pilha1.push(nota)
                            break
                        elif nota > 10:
                            print("Nota não pode ser maior que 10")
                            print("Tente novamente")
                        else:
                            print("Nota não pode ser negativa")
                            print("Tente novamente")
                elif op2 == 2:
                    while True:
                        nota = (float(input("\nDigite a nota:")))
                        if nota >= 0 and nota <= 10:
                            pilha2.push(nota)
                            break
                        elif nota < 10:
                            print("Nota não pode ser maior que 10")
                            print("Tente novamente")
                        else:
                            print("Nota não pode ser negativa")
                            print("Tente novamente")
                elif op2 == 3:
                    break
                else:
                    print("Opção invalida")

        elif op == 2:
            while True:
                op3 = int(input ("\nOpções:\n"
                                "1-Meninos\n"
                                "2-Meninas\n"
                                "3-Voltar\n"
                                "Opção:"))
                if op3 == 1:
                    pilha1.pop()
                elif op3 == 2:
                    pilha2.pop()
                elif op3 == 3:
                    break
                else:
                    print("opção invalida:")
                
        elif op == 3:
            while True:
                op4 = int(input ("\nOpções:\n"
                                "1-Meninos\n"
                                "2-Meninas\n"
                                "3-Voltar\n"
                                "Opção:"))
                if op4 == 1:
                    pilha1.media()
                elif op4 == 2:
                    pilha2.media()
                elif op4 == 3:
                    break
                else:
                    print("Opção invalida")

        elif op == 4:
            while True:
                op5 = int(input ("\nOpções:\n"
                                "1-Meninos\n"
                                "2-Meninas\n"
                                "3-Ambos\n"
                                "4-Voltar\n"
                                "Opção:"))
                if op5 ==1:
                    pilha1.printall()
                elif op5 == 2:
                    pilha2.printall()
                elif op5 == 3:
                    pilha3 = Pilha()
                    temp = pilha2.getTopo()
                    if temp:
                        while temp:
                            pilha3.push(temp.getValor())
                            temp = temp.getProximo()
                        pilha3.push("Meninas")
                        temp = pilha2.getTopo()
                    temp = pilha1.getTopo()
                    if temp:
                        while temp:
                            pilha3.push(temp.getValor())
                            temp = temp.getProximo()
                        pilha3.push("Meninos")
                        temp = pilha1.getTopo()
                    else:
                        print("pilha vazia")

                    pilha3.printall()
                   
                elif op5 == 4:
                    break
                else:
                    print("Opção invalida")

        elif op == 5:
            break

    del pilha2
    del pilha1

if __name__ == '__main__':
    main()