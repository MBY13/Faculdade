# Faça um programa para cadastrar funcionários.                                                         FEITO
# Para cada funcionário devem ser armazenados o nome, o salário e a idade.                              FEITO
# Os dados devem ser guardados em uma TAD lista simplesmente encadeada ordenada (não circular),         FEITO
# em ordem crescente pelo salário. menor pro maior                                                      FEITO
# O programa deve permitir a inclusão, exclusão e listagem com o valor médio dos salários e da idade,   FEITO
# além dos funcionários com salário abaixo da média (listando o nome, salário e idade).
# Obs: A resposta aceita texto na caixa de texto.

class No_lista:
    def __init__(self):
        self.__idade = 0
        self.__nome = None
        self.__salario = 0,0
        self.__proximo = None 

    def setidade(self,i):
        self.__idade = i
    def getidade(self):
        return self.__idade

    def setnome(self, n):
        self.__nome = n
    def getnome(self):
        return self.__nome

    def setsalario(self,s):
        self.__salario = s
    def getsalario(self):
        return self.__salario

    def setproximo(self, p):
        self.__proximo = p
    def getproximo(self):
        return self.__proximo

class Minha_lista_encadeada_ordenada:
    def __init__(self):
        self.__inicio = None

    def push(self, nome, idade, salario):
        novo = No_lista()
        if novo:
            novo.setnome(nome)
            novo.setidade(idade)
            novo.setsalario(salario)
            if self.__inicio:
                if novo.getsalario() <= self.__inicio.getsalario():
                    novo.setproximo(self.__inicio)    
                    self.__inicio = novo                
                else:
                    proximo = self.__inicio            
                    while True:
                        if proximo.getproximo():
                            if novo.getsalario() <= proximo.getproximo().getsalario():
                                novo.setproximo(proximo.getproximo())
                                proximo.setproximo(novo)
                                break
                            proximo = proximo.getproximo()        
                        else:
                            proximo.setproximo(novo)     
                            break
            else:
                novo.setproximo(None)
                self.__inicio = novo        

    def pop(self, nome):
        if self.__inicio:
            temp = self.__inicio
            if nome == temp.getnome():
                self.__inicio = temp.getproximo()
                print("inicio", self.__inicio.getnome())
                return
            while temp.getproximo():
                if nome == temp.getproximo().getnome(): 
                    temp.setproximo(temp.getproximo().getproximo())
                    return
                temp = temp.getproximo()
            print("nome", nome, "não encontrado.")
        else:
            print("Lista vazia, não pode remover.")

    def print_all(self):
        if self.__inicio:
            saida = "\n\nLista: \n"
            aux = self.__inicio
            while aux:
                saida += str(f"Nome:{aux.getnome()}\n"
                             f"Idade:{aux.getidade()} anos\n"
                             f"Salario R${aux.getsalario()}\n\n")
                aux = aux.getproximo()
            print(saida, "\n\n")
        else: 
            print("Não há funcionarios na lista.")

    def pop_all(self):
        if not self.__inicio:
            print("\n\nLista já está vazia: \n")
            return
        self.__inicio = None
        print("Lista está vazia agora")

    def mediasalario(self):
        if self.__inicio:
            cont = 0
            sal = 0.0
            aux = self.__inicio
            while aux:
                cont +=1
                sal += float(aux.getsalario())
                aux = aux.getproximo()
            mediasal = sal / cont
            print (f"Media dos Salairo R${mediasal}")
        else:
            print("Lista Vazia")

    def mediaidade(self):
        if self.__inicio:
            cont = 0
            idad = 0
            aux = self.__inicio
            while aux:
                cont +=1
                idad += int(aux.getidade())
                aux = aux.getproximo()
            mediaida = idad / cont
            print (f"Media dos Salairo R${mediaida}")

    def consultar(self, nome_consultado):
        if self.__inicio:
            saida = None
            lista_aux = self.__inicio
            while lista_aux:
                if lista_aux.getnome().upper() == nome_consultado:
                    saida = lista_aux.getsalario()
                lista_aux = lista_aux.getproximo()
        else: 
            print("Não há funcionarios na lista.")
        return saida

def main():
    op = 0 
    lista = Minha_lista_encadeada_ordenada()
    while True:
        op = int(input("Opções:\n"
                    "1 - Cadastrar Funcionarios.\n"
                    "2 - Funcionario a ser excluido\n"
                    "3 - Imprimir todos os funcionarios\n"
                    "4 - Exclui todos os funcionarios\n"
                    "5 - Media de Salario e idade\n"
                    "7 - Sair\n"
                    "opção:"))
        
        if op == 1:
            nome = input("Informe o nome do funcionario:")
            Idade = int(input("Informe a idade do funcionario:"))
            salario = float(input("Informe o salario do funcionario R$"))
            lista.push(nome, Idade, salario)
        
        elif op == 2:
            nome = input("Digite o nome que deseja remover:")
            lista.pop(nome)
        elif op == 3:
            lista.print_all()
        elif op == 4:
            lista.pop_all()

        elif op == 5:
            lista.mediasalario()
            lista.mediaidade()
        
        elif op == 7:
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
  main()