# contrua um programa com uma função para concatenar duas
# listas encadeadas l1 e L2 em uma unica lista encadeada ordenada
# depois, inclua uma função para remover os elementos repetidos
# da lista encadeada ordenada

# nãp devem ser alocados(criados) novos nós, os nós serao 
# religados para compor a nova lista ordenada

class No:
    def __init__(self):
        self.__numero = None
        self.__prox = None

    def getNumero(self):
        return self.__numero
    def setNumero(self, i):
        self.__numero = i

    def getProx(self):
        return self.__prox
    def setProx(self, p):
        self.__prox = p

class L:
    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push_end(self):
        Temp = No()
        if Temp:
            Temp.setNumero(int(input("Informe um número: ")))
            if self.__fim:
                self.__fim.setProx(Temp)
                self.__fim = Temp
            else:
                self.__ini = self.__fim = Temp

    def push_first(self):
        Temp = No()
        if Temp:
            Temp.setNumero(int(input("Informe um número: ")))
            Temp.setProx(self.__ini)
            if not self.__ini:
                self.__fim = Temp
            self.__ini = Temp

    def pop(self):
        if not self.__fim:
            print("Lista Vazia!")
            return
        num = int(input("Deseja excluir qual elemento? "))
        temp = self.__ini
        if temp.getNumero() is num:
            self.__ini = self.__ini.getProx()
            if not self.__ini:
                self.__fim = None
            return
        while temp.getProx():
            if temp.getProx().getnumero() is num:
                temp.setProx(temp.getProx().getProx())
                if not temp.getProx():
                    self.__fim = temp
                break
            temp = temp.getProx()

    def pop_all(self):
        if self.__ini is None:
            print("Lista Vazia!")
            return
        self.__ini = self.__fim = None
        print("Todos os itens da L removidos!")

    def print_all(self):
        if not self.__ini:
            print("Lista Vazia!")
            return
        saida = "\nLista\n"
        temp_no = self.__ini

        while temp_no:
            saida += "No: " + str(temp_no) + "   Valor: " + str(temp_no.getNumero()) + "  Prox: " + str(temp_no.getProx()) + "\n"
            temp_no = temp_no.getProx()
        print(saida)

class L3:
    def __init__(self,ListaL,ListaL2):
        self.__ini = None
        self.__fim = None
        L3.pop_L_push_L3(self, ListaL._L__ini)
        L3.pop_L_push_L3(self, ListaL2._L__ini)

    def pop_L_push_L3(self, ini):
        Temp = ini
        while Temp:
            Next = Temp.getProx()
            # Primeiro
            if not self.__ini:
                Temp.setProx(None)
                self.__ini = self.__fim = Temp
            elif Temp.getNumero() <= self.__ini.getNumero():    # insere no inicio
                Temp.setProx(self.__ini)
                self.__ini = Temp
            elif Temp.getNumero() >= self.__fim.getNumero():    # insere no final
                self.__fim.setProx(Temp)
                self.__fim = Temp
                Temp.setProx(None)
            else:
                pant = self.__ini
                while True:
                    if Temp.getNumero() <= pant.getProx().getNumero():  # no meio
                        Temp.setProx(pant.getProx())
                        pant.setProx(Temp)
                        break
                    pant = pant.getProx()
            Temp = Next

    def push(self):
        Temp = No()
        if Temp:
            Temp.setNumero(int(input("Informe um número: ")))
            # Primeiro
            if not self.__ini:
                Temp.setProx(None)
                self.__ini = self.__fim = Temp
            elif Temp.getNumero() <= self.__ini.getNumero():    # insere no inicio
                Temp.setProx(self.__ini)
                self.__ini = Temp
            elif Temp.getNumero() >= self.__fim.getNumero():    # insere no final
                self.__fim.setProx(Temp)
                self.__fim = Temp
                Temp.setProx(None)
            else:
                pant = self.__ini
                while True:
                    if Temp.getNumero() <= pant.getProx().getNumero():  # no meio
                        Temp.setProx(pant.getProx())
                        pant.setProx(Temp)
                        break
                    pant = pant.getProx()

    def pop(self,rep):
        if not self.__fim:
            print("Lista Vazia!")
            return
       # num = int(input("Deseja excluir qual elemento? "))
        num = rep
        temp = self.__ini
        if temp.getNumero() == num:
            self.__ini = self.__ini.getProx()
            if not self.__ini:
                self.__fim = None
            return
        while temp.getProx():
            if temp.getProx().getNumero() == num:
                temp.setProx(temp.getProx().getProx())
                if not temp.getProx():
                    self.__fim = temp
                break
            temp = temp.getProx()

    def pop_all(self):
        if not self.__ini:
            print("Lista Vazia!")
            return
        self.__ini = self.__fim = None
        print("Todos os itens da lista removidos!")

    def print_all(self):
        if not self.__ini:
            print("Lista Vazia!")
            return
        saida = "\nLista\n"
        temp_no = self.__ini

        while temp_no:
            saida += "No: " + str(temp_no) + "   Valor: " + str(temp_no.getNumero()) + "  Prox: " + str(temp_no.getProx()) + "\n"
            temp_no = temp_no.getProx()
        print(saida)

    def iguais (self):
        if not self.__ini:
            print("Lista vazia")
            return
        temp_no = self.__ini

        while temp_no:
            if temp_no.getNumero() == temp_no.getProx().getNumero():
                self.pop(temp_no.getNumero())

            if temp_no.getProx().getProx():
                temp_no = temp_no.getProx()
            else:
                break
###############################################################################################################
def menu():
    op = 0
    while True:
        op = int(input("\nMenu para a Lista L1\n"
                       "1 - Adicionar no Início\n"
                       "2 - Adicionar no Fim\n"
                       "3 - Remover um item\n"
                       "4 - Consultar uma lista\n"
                       "5 - Remover todos os itens\n"
                       "6 - Adicionar dados na segunda lista\n"
                       "Opção:"))
        if (op >= 1) and (op <= 6):
            break
    return op 

def menu2():
    op = 0
    while True:
        op = int(input("\nMenu para a Lista L2\n"
                       "1 - Adicionar no Início\n"
                       "2 - Adicionar no Fim\n"
                       "3 - Remover um item\n"
                       "4 - Consultar uma lista\n"
                       "5 - Remover todos os itens\n"
                       "6 - Concatenar listas\n"
                       "Opção:"))
        if (op >= 1) and (op <= 6):
            break
    return op 

def menu3():
    op = 0
    while True:
        op = int(input("\nMenu para a Lista Concatenada\n"
                       "1 - Adicionar Item\n"
                       "2 - Remover um item\n"
                       "3 - Consultar uma lista\n"
                       "4 - Remover todos os itens\n"
                       "5 - Sair\n"
                       "Opção:"))
        if (op >= 1) and (op <= 5):
            break
    return op 

l1 = L()
op = 0
while True:
    op = menu()
    if op == 1:
        l1.push_first()
    elif op == 2:
        l1.push_end()
    elif op == 3:
        l1.pop(int(input("Deseja excluir qual elemento? ")))
    elif op == 4:
        l1.print_all()
    elif op == 5:
        l1.pop_all()
    elif op == 6:
        l2 = L()
        while True:
            op = menu2()
            if op == 1:
                l2.push_first()
            elif op == 2:
                l2.push_end()
            elif op == 3:
                l2.pop(int(input("Deseja excluir qual elemento? ")))
            elif op == 4:
                l2.print_all()
            elif op == 5:
                l2.pop_all()
            elif op == 6:
                l3 = L3(l1,l2)
                l3.iguais()
                while True:
                    op = menu3()
                    if op == 1:
                        l3.push()
                    elif op == 2:
                        l3.pop(int(input("Deseja excluir qual elemento? ")))
                    elif op == 3:
                        l3.print_all()
                    elif op == 4:
                        l3.pop_all()
                    elif op == 5:
                        break
                    else:
                        print("Opcao inválida")
                break
            else:
                print('Opcao inválida')
        break
    else:
        print('Opcao inválida')