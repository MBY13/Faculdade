class No_pilha: #criamos um nó
    
    __numpilha = None            
    __proxpilha = None

    def __init__(self):#criação das variaveis
        self.__numpilha = 0
        self.__proxpilha = 0
    
    def setnumpilha(self,n):#inserir dados na variavel privada
        self.__numpilha = n
    def getnumpilha(self):#ler dados da variavel privada
        return self.__numpilha
    
    def setproxpilha(self , p):#inserir dados na variavel privada
        self.__proxpilha = p 
    def getproxpilha(self):#ler dados da variavel privada
        return self.__proxpilha

class Pilha:
    
    __topo = None

    def __init__(self):#criação das variaveis
        self.__topo = 0
    
    def push(self):#inserir informações no topo 
        novo = No_pilha() #criamos o objeto 
        if novo:
            novo.setnumpilha(int(input("Digite um numero inteiro (0 ou menor para parar de digitar):")))#colocamos o dado dentro do objeto 
            if self.__topo:
                novo.setproxpilha(self.__topo)#definimos o proximo campo
            self.__topo = novo

    def pop(self):#Exclui informações do topo
        if self.__topo:#verificando se a pilha não esta vazia
            self.__topo = self.__topo.getproxpilha()#excuindo
        else:
            print("\nPilha está vazia!")
    
    def printall(self):#printar tudo
        if self.__topo:#verificando se a pilha não esta vazia
            saida = '\n====Todos os numeros digitados====\n'
            temp = self.__topo #variavel local para pegar o topo
            while temp:
                saida += (f"{str(temp.getnumpilha())}\n")
                temp = temp.getproxpilha()#proximo topo
            print(saida)#printamos todos os dados
        else:
            print('\nPilha vazia')
    
    def printtop(self):
        if self.__topo:
            self.__topo = self.__topo.getnumpilha()
            print (self.__topo)
    
    def returntopo(self):
        return self.__topo.getnumpilha()
class No_fila:

    __numfila = None            
    __proxfila  = None

    def __init__(self):#criação das variaveis
        self.__numfila = 0
        self.__proxfila = 0
    
    def setnumfila(self,n):#inserir dados na variavel privada
        self.__numfila = n
    def getnumfila(self):#ler dados da variavel privada
        return self.__numfila
    
    def setproxfila(self , p):#inserir dados na variavel privada
        self.__proxfila = p 
    def getproxfila(self):#ler dados da variavel privada
        return self.__proxfila

class Fila:

    __ini = None
    __fim = None

    def __init__(self):#criação das variaveis
        self.__ini = 0
        self.__fim = 0

    def push(self,numero):#inseri informações para ficar em fila
        temp = No_fila()#criamos o objeto
        if temp:
            temp.setnumfila(numero)#colocamos o dado dentro do objeto 
            if not self.__ini:
                self.__ini = self.__fim = temp  
            else:  
                self.__fim.setproxfila(temp)#definimos o proximo campo
                self.__fim = temp
    
    def pop(self):#Exclui informações da fila
        if self.__fim: #verificando se a fila não esta vazia
            if self.__ini:  
                self.__ini = self.__ini.getproxfila()#excuindo
                if not self.__ini:
                    self.__fim = None
        else:
            print('\nFila vazia')

    def printall(self):#printar tudo
        if self.__fim:#verificando se a fila não esta vazia
            temp = self.__ini#variavel local para pegar as informações da fila
            saida = "=====Numeros======\n"
            while temp:
                saida += str(f"{str(temp.getnumfila())}\n")
                temp = temp.getproxfila()#proximo da fila 
            print(saida)#printamos todos os dados
        else:
            print('\nFila vazia')

def main():

    numeros = Pilha() #pila
    pares = Fila() #fila
    impares = Fila() #fila

    while True:

        op = int(input("\n====Opções====\n"#menu
                    "1-Entre com dados\n"
                    "2-Fila Par\n"
                    "3-Fila Impar\n"
                    "4-Todos os numeros digitados\n"
                    "5-Finalizar\n"
                    "Opção:"))
        
        if op == 1:

            while True:
                
                numeros.push()

                if numeros.returntopo() == 0: #encerramemnto do programa
                    numeros.pop()
                    break

                if numeros.returntopo() %2 == 0:# par 
                    pares.push(numeros.returntopo())
                    
                else:
                    impares.push(numeros.returntopo())#impar

        elif op ==2:
            pares.printall()#par
        elif op == 3:
            impares.printall()#impar
        elif op == 4:
            numeros.printall()#todos
        elif op == 5:
            break
        else:
            print("Opção digitada invalida!")

if __name__ == '__main__':
    main()