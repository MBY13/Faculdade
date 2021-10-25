import sys

class Roupa:
    __Roupa_Marca = None
    __Roupa_Cor = None
    __Roupa_Tam = None
    __Roupa_Quant = None
    __Roupa_Preco = None
    __Total_Roupa = None

    def __init__(self):
        self.__Roupa_Marca = " "
        self.__Roupa_Cor = " "
        self.__Roupa_Tam = 0
        self.__Roupa_Quant = 0
        self.__Roupa_Preco = 0.0 
        self.__Total_Roupa = 0.0

    def Leitura(self):
        self.__Roupa_Marca =(input("Digite a marca da roupa:"))
        self.__Roupa_Cor = (input("Digite a cor da roupa:"))
        self.__Roupa_Tam = int(input("Digite o tamanho da roupa:"))
        self.__Roupa_Quant = int(input("Digite a quantidade de roupa:"))
        self.__Roupa_Preco = float(input("Digite o valor da roupa (.00):"))

    def Calcula_Total(self):
        self.__Total_Roupa = self.__Roupa_Quant * self.__Roupa_Preco

    def toString(self):
        Str = " "
        Str = (f"Marca da Roupa : {self.__Roupa_Marca}\n"
               f"Cor da Roupa : {self.__Roupa_Cor}\n"
               f"Tamanho da Roupa : {self.__Roupa_Tam}\n"
               f"Quantidade de Roupa :{self.__Roupa_Quant}\n"
               f"Preço da Roupa R${self.__Roupa_Preco}\n"
               f"Valor total da compra R${self.__Total_Roupa}\n")
        return Str

aa  = Roupa()
aa.Leitura()
aa.Calcula_Total()
print(aa.toString())

sys.exit(0)