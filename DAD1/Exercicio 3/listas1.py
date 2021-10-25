# Construa um programa para ler uma palavra, imprimindo-a em ordem inversa. 
# Uma pilha de letras será usada para inverter a palavra. 
# Primeiro, os caracteres são extraídos um por um da cadeia de entrada e empilhados. 
# Então eles são desempilhados e exibidos. 
# Por causa da característica LIFO, a pilha inverte a ordem dos caracteres. 

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
    
def main():
    palavra = Pilha()
    palavra.push()
    print(palavra.lifo())
    print (f'A palavra inversa é:{palavra.lifo()}')

if __name__ == "__main__":
    main()