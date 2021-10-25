class pilha:

    def __init__(self):
        self.__altura = 0.0
        self.__peso = 0.0
        self.__imc = []

    def push(self):
        self.__altura = (float(input("Digite a altura do aluno:")))
        self.__peso = (float(input("Digite o peso do aluno:")))
        self.imc()

    def pop(self):
        if self.__imc:
            del self.__imc[len(self.__imc)-1]
        else:
            print("Pilha vazia!")

    
    def imc(self):
        self.__imc.append(self.__peso/(self.__altura * self.__altura))

    def print_top(self):
        if self.__imc:
            print (self.__imc[len(self.__imc)-1])
        else:
            print("Pilha vazia!")


def main():
    Aluno = pilha()

    while True:
        op = int(input("Opção\n"
                   "1 - Cadastro do IMC\n"
                   "2 - Deleta o ultimo IMC\n"
                   "3 - Imprime o ultimo IMC\n"
                   "4 - Sair\n"
                   "Digite a opção:"))
        if op == 1:
            Aluno.push()
        elif op == 2:
            Aluno.pop()
        elif op == 3:
            Aluno.print_top()
        elif op == 4:
            print("O programa encerrou!")
            break
        else:
            print("Opção Invalida")

if __name__ == "__main__":
    main()