#Escreva um programa usando pilhas para determinar se uma string é um palíndromo.

class Pilha:

    def __init__(self):
        self.__palavra = []
        self.__letras = []

    def push(self):
        self.__palavra.append(input("Digite a palavra para imprimir ela inversa:"))

    def lifo(self):
        if self.__palavra:
            for palavra in self.__palavra:
                auxiliar = []
                separado= []
                resultado = ""
                for a in palavra:
                    auxiliar.append(a)
            while auxiliar:
                separado.append(auxiliar[len(auxiliar)-1])
                del auxiliar[len(auxiliar)-1]
            for x in separado:
                resultado += x
            self.__letras.append(resultado)
            return self.__letras
        else:
            print("A PILHA ESTA VAZIA!")

    def igualdade(self):
        self.lifo()
        if self.__palavra == self.__letras:
            print("A palavra digitada é um Palídromo")
        else: 
            print("A palavra digitada não é um palindromo")

def main():
    palavra = Pilha()
    palavra.push()
    palavra.igualdade()
if __name__ == "__main__":
    main()