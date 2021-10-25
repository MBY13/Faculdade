# Exerc 6, a partir de Lista encadeada L desordenada,
# tenha uma função que cria uma nova Lista K ordenada,
# com os mesmos nós da Lista L.

class No:
    def __init__(self):
        self.__inteiro = None
        self.__prox = None
    def getInteiro(self):
        return self.__inteiro
    def setInteiro(self, inteiro):
        self.__inteiro = inteiro
    def getProx(self):
        return self.__prox
    def setProx(self, prox):
        self.__prox = prox


class L:
    def __init__(self):
        self.__ini = None
        self.__fim = None

    def push_end(self):
        Temp = No()
        if Temp:
            Temp.setInteiro(int(input("Informe um número: ")))
            if self.__fim:
                self.__fim.setProx(Temp)
                self.__fim = Temp
            else:
                self.__ini = self.__fim = Temp
            L.print_all(self)

    def push_first(self):
        Temp = No()
        if Temp:
            Temp.setInteiro(int(input("Informe um número: ")))
            Temp.setProx(self.__ini)
            if not self.__ini:
                self.__fim = Temp
            self.__ini = Temp
            L.print_all(self)

    def pop(self):
        if not self.__fim:
            print("Lista Vazia!")
            return
        L.print_all(self)
        num = int(input("Deseja excluir qual elemento? "))
        temp = self.__ini
        if temp.getInteiro() is num:
            self.__ini = self.__ini.getProx()
            if not self.__ini:
                self.__fim = None
            L.print_all(self)
            return
        while temp.getProx():
            if temp.getProx().getInteiro() is num:
                temp.setProx(temp.getProx().getProx())
                if not temp.getProx():
                    self.__fim = temp
                break
            temp = temp.getProx()
        L.print_all(self)

    def pop_all(self):
        if self.__ini is None:
            print("Lista Vazia!")
            return
        self.__ini = self.__fim = None
        print("Todos os itens da L removidos!")
        L.print_all(self)

    def print_all(self):
        if not self.__ini:
            print("Lista Vazia!")
            return
        saida = "\nLista\n"
        temp_no = self.__ini

        while temp_no:
            saida += "No: " + str(temp_no) + "   Valor: " + str(temp_no.getInteiro()) + "  Prox: " + str(temp_no.getProx()) + "\n"
            temp_no = temp_no.getProx()
        print(saida)


class K:
    def __init__(self, ListaL):
        self.__ini = None
        self.__fim = None
        K.pop_L_push_K(self, ListaL._L__ini)

    def pop_L_push_K(self, ini):
        Temp = ini
        while Temp:
            Next = Temp.getProx()
            # Primeiro
            if not self.__ini:
                Temp.setProx(None)
                self.__ini = self.__fim = Temp
            elif Temp.getInteiro() <= self.__ini.getInteiro():    # insere no inicio
                Temp.setProx(self.__ini)
                self.__ini = Temp
            elif Temp.getInteiro() >= self.__fim.getInteiro():    # insere no final
                self.__fim.setProx(Temp)
                self.__fim = Temp
                Temp.setProx(None)
            else:
                pant = self.__ini
                while True:
                    if Temp.getInteiro() <= pant.getProx().getInteiro():  # no meio
                        Temp.setProx(pant.getProx())
                        pant.setProx(Temp)
                        break
                    pant = pant.getProx()
            Temp = Next

    def push(self):
        Temp = No()
        if Temp:
            Temp.setInteiro(int(input("Informe um número: ")))
            # Primeiro
            if not self.__ini:
                Temp.setProx(None)
                self.__ini = self.__fim = Temp
            elif Temp.getInteiro() <= self.__ini.getInteiro():    # insere no inicio
                Temp.setProx(self.__ini)
                self.__ini = Temp
            elif Temp.getInteiro() >= self.__fim.getInteiro():    # insere no final
                self.__fim.setProx(Temp)
                self.__fim = Temp
                Temp.setProx(None)
            else:
                pant = self.__ini
                while True:
                    if Temp.getInteiro() <= pant.getProx().getInteiro():  # no meio
                        Temp.setProx(pant.getProx())
                        pant.setProx(Temp)
                        break
                    pant = pant.getProx()
            K.print_all(self)

    def pop(self):
        if not self.__fim:
            print("Lista Vazia!")
            return
        K.print_all(self)
        num = int(input("Deseja excluir qual elemento? "))
        temp = self.__ini
        if temp.getInteiro() == num:
            self.__ini = self.__ini.getProx()
            if not self.__ini:
                self.__fim = None
            K.print_all(self)
            return
        while temp.getProx():
            if temp.getProx().getInteiro() == num:
                temp.setProx(temp.getProx().getProx())
                if not temp.getProx():
                    self.__fim = temp
                break
            temp = temp.getProx()
        K.print_all(self)

    def pop_all(self):
        if not self.__ini:
            print("Lista Vazia!")
            return
        self.__ini = self.__fim = None
        print("Todos os itens da lista removidos!")
        K.print_all(self)

    def print_all(self):
        if not self.__ini:
            print("Lista Vazia!")
            return
        saida = "\nLista\n"
        temp_no = self.__ini

        while temp_no:
            saida += "No: " + str(temp_no) + "   Valor: " + str(temp_no.getInteiro()) + "  Prox: " + str(temp_no.getProx()) + "\n"
            temp_no = temp_no.getProx()
        print(saida)
######################################################


def menu():
    while True:
        str = "Menu de Opções - Lista L\n"
        str += "1 - Adicionar item no fim\n"
        str += "2 - Adicionar item no início\n"
        str += "3 - Remover item\n"
        str += "4 - Consultar a Lista\n"
        str += "5 - Remover todos os itens\n"
        str += "6 - Converter para Lista Ordenada\n\n"
        str += "Opção:"
        op = int(input(str))
        if (op >= 1) and (op <= 6):
            break
    return op

def menu2():
    while True:
        str = "Menu de Opções - Lista K\n"
        str += "1 - Adicionar item\n"
        str += "2 - Remover item\n"
        str += "3 - Consultar a Lista\n"
        str += "4 - Remover todos os itens\n"
        str += "5 - Sair\n\n"
        str += "Opção:"
        op = int(input(str))
        if (op >= 1) and (op <= 5):
            break
    return op

l = L()
op = 0
while True:
    op = menu()
    if op == 1:
        l.push_end()
    elif op == 2:
        l.push_first()
    elif op == 3:
        l.pop()
    elif op == 4:
        l.print_all()
    elif op == 5:
        l.pop_all()
    elif op == 6:
        k = K(l)
        while True:
            op = menu2()
            if op == 1:
                k.push()
            elif op == 2:
                k.pop()
            elif op == 3:
                k.print_all()
            elif op == 4:
                k.pop_all()
            elif op == 5:
                break
            else:
                print("Opcao inválida")
        break
    else:
        print('Opcao inválida')
