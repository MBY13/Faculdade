# Em um cassino, existe uma máquina de caça níqueis que 
# dará 1 milhão de dólares. 
# Porém, é permitido que os jogadores apostem apenas 
# uma única vez e depois voltem para o final da fila. Em cada 
# jogada, os jogadores gastam 5 dólares. 
# Faça um programa que simule o caça-níquel e a cada requisição subtraia 5 dólares do participante. Quando o valor em 
# dólares for menor que 5 o participante deve ser retirado da fila.
# Utilize uma fila circular para armazenar os dados. 
# Sabe-se que desde o início do seu funcionamento naquela noite, 
# que haverá um premiado em uma determinada jogada.
# Quem ganhou 1 milhão de dólares?

from math import trunc
from random import randint
from time import thread_time

class No_fila:
    __nome = None
    __proximo = None 
    __saldo = None
    __ganhador = None

    def __init__(self):
        self.__nome = " "
        self.__proximo = 0
        self.__saldo = 0.0
        self.__ganhador = 0

    def getnome(self):
        return self.__nome
    def setnome(self, n):
        self.__nome = n

    def setproximo(self, p):
        self.__proximo = p  
    def getproximo(self):
        return self.__proximo

    def setsaldo(self, s):
        self.__saldo = s  
    def getsaldo(self):
        return self.__saldo        

    def setganhador(self):
        self.__ganhador = randint(0,10) 
    def getganhador(self):
        return self.__ganhador

class Fila:
    def __init__(self):
        self.__final = None

    def push(self,nome,saldo):
        temp = No_fila()
        if temp:
            temp.setnome(nome)
            temp.setsaldo(saldo)
            temp.setganhador()
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
            saldo = self.__final.getproximo().getsaldo()          
            if (self.__final.getproximo() == self.__final):                
                self.__final = None
            else:
                proximo = self.__final.getproximo().getproximo()
                self.__final.setproximo(proximo)
            print("Nome removido: ", nome,"\n"
                  "Saldo $",saldo)
        else:
            print("Fila vazia")

    def print_all(self):
        if self.__final:       
            temp = No_fila() 
            temp = self.__final.getproximo()
            saida = " \nFila circular:\n"  
            while temp != self.__final:   
                saida +=(f"\tNome:{temp.getnome()}\n"
                         f"\tSaldo ${temp.getsaldo()}\n")   
                temp = temp.getproximo()         
            print(saida,
                 f"\tNome:{temp.getnome()}\n"
                 f"\tSaldo ${temp.getsaldo()}\n")      
        else:
            print("Fila vazia")

    def caca_niquel(self):
        if self.__final:
            temp = No_fila() 
            temp = self.__final.getproximo()
            aux = self.__final
            while temp != aux:
                if temp.getsaldo() < 5.0:
                    self.pop()
                else:
                    temp.setsaldo(temp.getsaldo() - 5)
                    if self.luck():
                        break
                    self.push(temp.getnome(),temp.getsaldo())
                    self.pop()
                temp = temp.getproximo() 
            if temp.getsaldo() < 5.0:
                self.pop()
            else:
                temp.setsaldo(temp.getsaldo() - 5) 
                self.luck()
                self.push(temp.getnome(),temp.getsaldo())
                self.pop()
            print("Saldo atualizado depois de uma jogada")
            self.print_all()

    def luck (self):
        if self.__final:
            nome = self.__final.getproximo().getnome()     
            saldo = ((self.__final.getproximo().getsaldo()) + 1000000.00)
            jogador = randint(0,10) 
            if jogador == self.__final.getproximo().getganhador():
                print("Temos um ganhador")
                print("Nome: ", nome,"\n"
                  "Saldo $",saldo)
                self.__final.getproximo().setsaldo(saldo)
                a = True
                return a 
            else: 
                a = False
                return a 

def main():
    fila = Fila()
    while True:
        op = int(input("1 - Inserir Jogadores\n"
                       "2 - Imprimir Jogadores\n"
                       "3 - Jogar\n"
                       "4 - Sair"
                       "\nOpção:"))            
        if op == 1:
            print("\n")
            nome = input("Informe o nome:")
            saldo = float(input("Digite o Valor que o jogador tem de saldo $"))
            fila.push(nome,saldo)
        elif op == 2:
            fila.print_all()
        elif op == 3:
            fila.caca_niquel()
        elif op == 4:
            break
        else:
            print("Opcao invalida.")

if __name__ == '__main__':
    main() 