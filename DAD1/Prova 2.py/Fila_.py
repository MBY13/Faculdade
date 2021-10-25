import time

class Node:
    def __init__(self):
        self.__nome = input('Digite o Nome: ')
        self.__prox = None

    def getnome(self):
        return self.__nome
    def setnome(self, n):
        self.__nome = n

    def getprox(self):
        return self.__prox
    def setprox(self, p):
        self.__prox = p
    
    def setsenha(self, s):
        self.__senha = s
    def getsenha(self):
        return self.__senha

    def sethora(self):
        self.__hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
    def gethora(self):
        return self.__hora

class Fila:

    def __init__(self):
        self.__ini = None
        self.__fim = None
        self._iniA = None

    def push(self, senha):
        temp = Node()
        temp.setsenha(senha)
        if temp:
            if not self.__ini:
                self.__ini = self.__fim = temp
            else:
                self.__fim.setprox(temp)
                self.__fim = temp

    def pop(self):
        if self.__ini:
            self.__ini = self.__ini.getprox()
            if not self.__ini:
                self.__fim = None
                print('O primeiro cliente da fila foi atendido!')
        else: 
            print('Fila Vazia')        
        

    def printall(self):
        if self.__fim:
            temp = self.__ini
            saida = ''
            while temp:
                saida += str('Nome: ' + temp.getnome() + '| Senha: ' + str(temp.getsenha()) + '\n')
                temp = temp.getprox()
            print(saida)
        else:
            print('A fila está vazia!')
            return False

    def senhas(self):
        if self.__fim:
            temp = self.__ini
            saida = "\nFila\n"
            while temp:
                saida += str('Nome: ' + temp.getnome() + '| Senha: ' + str(temp.getsenha()) + '\n')
                temp = temp.getprox()
        else:
            return False

        
fPref = Fila()
fNpref = Fila()
atend = Fila()
atendN = Fila()

preferencial = 0
npreferencial = 0

while True:

    op = int(input(f'\n=====As opções de menu são: ======\n'
        '1 - Senha para cliente preferencial.\n'
        '2 - Senha para cliente não preferencial.\n'
        '3 - Chamar para atendimento cliente.\n'
        '4 - Visualizar todos os clientes aguardando (não preferencial ou preferencial).\n'
        '5 - Visualizar fila de clientes atendidos (não preferencial ou preferencial).\n'))

    if op == 1:
        preferencial +=1
        fPref.push(preferencial)

    if op == 2:
        npreferencial +=1
        fNpref.push(npreferencial)

    if op == 3:
        if fPref.senhas() == False:
            fNpref.pop()
        else:
            fPref.pop()

    if op == 4:
        print('Fila Preferencial')
        fPref.printall()
        print('Fila Não Preferencial')
        fNpref.printall()

    if op == 5:
       pass