# Faça um programa de gerenciamento de ordem para atendimento ao cliente. 
# O cliente chegará para ser atendido, receberá uma senha sequencial e aguardará na fila até ser chamado.
#  A senha estará atrelada ao cartão fidelidade do cliente que possui nome e motivo do atendimento
#  (Gere a senha automaticamente e armazene todos os atributos no mesmo objeto).
# Ao ser chamado para atendimento, o primeiro cliente da fila é removido. 
# É possível que os atendentes confiram todos os dados referente aos clientes que estão aguardando na 
# fila (seguindo o conceito de fila, apenas o primeiro pode ser manipulado).
# Ao final do dia de trabalho, é necessário gerar um relatório onde constem todos os atendimento realizados 
# naquele período, com o horário de atendimento de cada cliente (Adicione um atributo ao cliente e manipule 
# uma fila a parte para gerar esse relatório).
# =====As opções de menu são: ======
# 1 - Receber cliente na fila.
# 2 - Chamar para atendimento.
# 3 - Visualizar fila de clientes aguardando.
# 4 - Visualizar fila de clientes atendidos.
# Obs: Lembre de indicar o horário de atendimento de cada cliente.
# Antes de sair programando, modele o diagrama de Classes. Pode ser no papel mesmo. Adicione o diagrama na entrega.
# Implemente a solução com fila sequencial e com fila encadeada.

class FilaCliente:
    __senha = None
    __horario = None 
    __senhacliente = None

    def __init__(self):
        self.__senha = 0
        self.__horario = []
        self.__senhacliente = []
    
    def push(self):
        self.__horario.append(input("Digite o horario de chegada do cliente (HH:MM):"))
        self.__senha += 1
        self.__senhacliente.append(self.__senha)
    
    def getsenhacliente(self,a):
        return self.__senhacliente[a]
    def gethorario(self,a):
        return self.__horario[a]

class CartãoFidelidade(FilaCliente):
    __cliente = None
    __motivo = None

    def __init__(self):
        super().__init__()
        self.__cliente = []
        self.__motivo = []
        cont = -1
    
    def push(self):
        super().push()
        self.__cliente.append(input("Digite o nome do cliente:"))
        self.__motivo.append(input("Digite o motivo da consulta:"))
    
    def pop(self,cont):
        del super().getsenhacliente(cont)
        del super().gethorario(cont)
        del self.__cliente[cont]
        del self.__motivo[cont]

    def printall(self,cont):
        if self.__cliente:
            Str = ""
            Str += (f"Cliente:{self.__cliente[cont]}\n"
                f"Senha:{super().getsenhacliente(cont)}\n"
                f"Motivo:{self.__motivo[cont]}\n"
                f"Horario{super().gethorario(cont)}\n")
            cont += 1
            return Str
        else:
            print("A FILA ESTA VAZIA!")

    def chamada(self,cont):
        super().getsenhacliente(cont)
        super().gethorario(cont)
        self.__cliente[cont]
        self.__motivo[cont]
