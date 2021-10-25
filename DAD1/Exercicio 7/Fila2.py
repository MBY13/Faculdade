import time

class Node:

    __nome = None
    __prox = None
    __motivo = None
    __senha = None
    __hora = None
    __ats = None

    def __init__(self):
        self.__nome = " "
        self.__prox =0
        self.__motivo = ""
        self.__senha = 0
        self.sethora()
        self.__ats = " "

    def getnome(self):
        return self.__nome

    def setnome(self, n):
        self.__nome = n

    def getprox(self):
        return self.__prox

    def setprox(self, p):
        self.__prox = p
    
    def getmotivo(self):
        return self.__motivo

    def setmotivo(self, m):
        self.__motivo = m

    def getsenha(self):
        return self.__senha

    def setsenha(self, s):
        self.__senha = s

    def sethora(self):
        self.__hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())

    def gethora(self):
        return self.__hora

    def getats(self):
        return self.__ats

    def setats(self, a):
        self.__ats = a

class Fila:

    __ini = None
    __fim = None
    __atend = None
    __inia = None
    __fima = None
    
    def __init__(self):
        self.__ini = 0
        self.__fim = 0
        self.__atend = 0
        self.__inia = 0
        self.__fima = 0
        
    def push(self,senha):
        temp = Node()
        if temp:
            temp.setnome(input("Digite o nome do paciente:"))
            temp.setmotivo(input("Digite o motivo da consulta:"))
            temp.setsenha(senha)
            temp.sethora()
            if not self.__ini:
                self.__ini = self.__fim = temp  
            else:  
                self.__fim.setprox(temp)
                self.__fim = temp
            Fila.printall(self)

    def pop(self):
        if self.__fim:
            if self.__ini:  
                self.__atend = self.__ini
                self.__ini = self.__ini.getprox()
                if not self.__ini:
                    self.__fim = None
            Fila.printall(self)
        else:
            print('Fila vazia')

    def printall(self):
        if self.__fim:
            temp = self.__ini
            saida = "=====Fila de espera======\n"
            while temp:
                saida += str(f"Senha :{temp.getsenha()}\n"
                             f"Nome :{temp.getnome()}\n"
                             f"Motivo :{temp.getmotivo()}\n"
                             f"Hora :{temp.gethora()}\n\n")
                temp = temp.getprox()
            print(saida)
        else:
            print('Fila vazia')
    
    def atendido(self):
        if self.__fim:
            self.pop()
            at = "=====atendido======\n"
            while self.__atend:
                at += str(f"Senha :{self.__atend.getsenha()}\n"
                          f"Nome :{self.__atend.getnome()}\n"
                          f"Motivo :{self.__atend.getmotivo()}\n"
                          f"Hora :{self.__atend.gethora()}\n")
                temp = Node()
                if temp:
                    temp.setats(at)
                    if not self.__inia:
                        self.__inia = self.__fima = temp  
                    else:  
                        self.__fima.setprox(temp)
                        self.__fima = temp
                    Fila.printall(self)
                break
            print (at)
        else:
            print('Fila vazia')
    
    def atendidos(self):
        if self.__fima:
            temp = self.__inia
            while temp:
                print (temp.getats())
                temp = temp.getprox()
        else:
            print('Fila vazia')

def main():

    cliente = Fila()
    senha = 0 

    while True:

        op = int(input("=====As opções de menu são:======\n"
                       "1 - Receber cliente na fila.\n"
                       "2 - Chamar para atendimento.\n"
                       "3 - Visualizar fila de clientes aguardando.\n"
                       "4 - Visualizar fila de clientes atendidos\n"
                       "5 - Sair\n"
                       "Opção:"))
        if op == 1:
            print ("\n")
            senha += 1
            cliente.push(senha)
        elif op == 2:
            print ("\n")
            cliente.atendido()
        elif op == 3:
            print ("\n")
            cliente.printall()
        elif op == 4:
            print ("\n")
            cliente.atendidos()
        elif op == 5:
            break
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()