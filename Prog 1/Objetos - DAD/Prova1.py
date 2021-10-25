import sys

class Medicamento:
    __Nome = None
    __Validade = None
    __Fabricante = None
    __preco = None
    __total = None
    __quant = None

    def __init__(self):
        self.__Nome = " "
        self.__Validade = " "
        self.__Fabricante = " "
        self.__preco = 0.0
        self.__quant = 0
        self.Calcular()

    def leitura(self):
        self.__Nome = (input("Digite o nome do medicamento:"))
        self.__Validade = (input("Digite a Validade do medicamento(dd/mm/aa):"))
        self.__Fabricante = (input("Digite o fabricante do medicamento:"))
        self.__preco = float(input("Digite o valor do medicamento R$"))
        self.__quant = int(input("Digite a Quantidade de remedios comprados:"))
    
    def Calcular(self):
        self.__total = self.__quant * self.__preco

    def toString(self):
        Str = " "
        Str = (f"\nNome do Medicamento:{self.__Nome}\n"
               f"Validade do Medicament:{self.__Validade}\n"
               f"Fabricante do Medicamento:{self.__Fabricante}\n"
               f"Quantidade comprada:{self.__quant}\n"
               f"Preço do Medicamento R${self.__preco}\n"
               f"Valor total da compra R${self.__total}\n")
        return Str
    
    def __del__(self):
        print ("Medicamento")

class Controlado(Medicamento):
    __Identidade = None
    __CRM = None
    __Vendedor = None

    def __init__(self):
        super().__init__()
        self.__Identidade = " "
        self.__CRM = " "
        self.__Vendedor = " "

    def leitura(self):
        super().leitura()
        self.__Identidade = (input("Digite a Identidade:"))
        self.__CRM = (input("Digite o CRM:"))
        self.__Vendedor = (input("Digite o nome do Vendedor:"))
    
    def toString(self):
        Str = (super().toString() +
                f"Identidade:{self.__Identidade}\n"
                f"CRM:{self.__CRM}\n"
                f"Vendedor:{self.__Vendedor}\n")
        return Str
    
    def __del__(self):
        super().__del__()
        print("Controlado")
##################################################################################################################
Contr = Controlado()
Contr.leitura()
Contr.Calcular()
print (Contr.toString())
del(Contr)

sys.exit(0)