#Faça um programa de gerenciamento de ordem para atendimento ao cliente. 
#O cliente chegará para ser atendido, receberá uma senha sequencial e aguardará na fila até ser chamado. A senha estará atrelada ao cartão fidelidade do cliente que possui nome e motivo do atendimento. (Gere a senha automaticamente e armazene todos os atributos no mesmo objeto).
#Ao ser chamado para atendimento, o primeiro cliente da fila é removido. 
#É possível que os atendentes confiram todos os dados referente aos clientes que estão aguardando na fila (seguindo o conceito de fila, apenas o primeiro pode ser manipulado).
#Ao final do dia de trabalho, é necessário gerar um relatório onde constem todos os atendimento realizados naquele período, com o horário de atendimento de cada cliente (Adicione um atributo ao cliente e manipule uma fila a parte para gerar esse relatório).
#=====As opções de menu são: ======
#1 - Receber cliente na fila.
#2 - Chamar para atendimento.
#3 - Visualizar fila de clientes aguardando.
#4 - Visualizar fila de clientes atendidos.
#Obs: Lembre de indicar o horário de atendimento de cada cliente.
#Antes de sair programando, modele o diagrama de Classes. Pode ser no papel mesmo. Adicione o diagrama na entrega.
#Implemente a solução com fila sequencial e com fila encadeada.
from datetime import datetime

class Fila:

    __pessoas = None
    __atendidos = None
    
    def __init__(self):
        self.__pessoas = []
        self.__atendidos = []

    def popfila(self):
        if self.__pessoas:
            print(f'Nome: {self.__pessoas[0].getNome()} | Senha: {self.__pessoas[0].getSenha()} | Horario de Atendimento: {self.__pessoas[0].getData()}')
            self.__atendidos.append(self.__pessoas[0].toString())
            del self.__pessoas[0]
        else:
            print('Não há ninguem na fila')
    
    def push(self, f):
        self.__pessoas.append(f)

    def printAll(self):
        temp = self.__pessoas.copy()
        
        while temp:
            print(temp[0].toString())
            del temp[0]
        del temp
    
    def printAtendidos(self): 
        temp = Fila()
        temp = self.__atendidos
        
        if self.__atendidos:
            while temp:
                print(temp[0])
                del temp[0]
        else:
            print('Ninguem foi atendido!')
        
        del temp

class cartaoFidelidade:

    __nome = None
    __motivo = None
    __senha = None
    __data = None

    def __init__(self):
        self.__nome = input('Digite o nome dos clientes: ')
        self.__motivo = input('Digite o motivo do cliente vir ao consultorio: ')
        self.__data = str(datetime.now().strftime('%H:%M'))
        self.toString()
        
    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        self.__senha = senha
    
    def getNome(self):
        return self.__nome
    
    def getMotivo(self):
        return self.__motivo
    
    def getData(self):
        return self.__data
    
    def toString(self):
        Str = (f'Nome: {self.__nome} | Senha: {self.__senha} | Hora: {self.__data} | Motivo: {self.__motivo}')
        return Str
    
def main():

    senhaGlobal = 0

    fila = Fila()

    while True:
        op = int(input(f'#=====As opções de menu são: ======\n'
        '1 - Adiciona cliente na fila\n'
        '2 - Chama cliente para atendimento\n'
        '3 - Clientes aguardando  para ser atendido\n'
        '4 - Clientes atendidos\n'
        '5 - Sair.\n'))

        if op == 1:
            senhaGlobal += 1
            example = cartaoFidelidade()
            example.setSenha(senhaGlobal)
            fila.push(example)
            print('\n')

        if op == 2:
            fila.popfila()
        
        if op == 3:
            fila.printAll()
        
        if op == 4:
            fila.printAtendidos()
        
        if op == 5:
            break
        
        else:
            print('Digite uma opção valida!')
                    
if __name__ == '__main__':
    main()