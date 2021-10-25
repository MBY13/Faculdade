import sys

class Roupa:

    __Roupa_Marca = None
    __Roupa_Cor = None
    __Roupa_Tam = None
    __Roupa_Quant = None
    __Roupa_Preco = None
    __Total_Roupa = None

    def __init__(self):
        self.__Roupa_Marca = ""
        self.__Roupa_Cor = ""
        self.__Roupa_Tam = 0
        self.__Roupa_Quant = 0
        self.__Roupa_Preco = 0.0
        self.__Total_Roupa = 0.0

    def leitura(self):
        self.__Roupa_Marca = (input("Digite a Marca:"))
        self.__Roupa_Cor = (input("Digite a cor:"))
        self.__Roupa_Tam =(int(input("Digite o tamanho:")))
        self.__Roupa_Quant=(int(input("Digite a quantidade:")))
        self.__Roupa_Preco =(float(input("Digite o preço R$")))
        self.calcula_total()

    def calcula_total(self):
        self.__Total_Roupa = self.__Roupa_Preco * self.__Roupa_Quant

    def toString(self):
        Str = " "
        Str = (f"\nMarca da Roupa : {self.__Roupa_Marca}\n"
               f"Cor da Roupa : {self.__Roupa_Cor}\n"
               f"Tamanho da Roupa : {self.__Roupa_Tam}\n"
               f"Quantidade de Roupa :{self.__Roupa_Quant}\n"
               f"Preço da Roupa R${self.__Roupa_Preco}\n"
               f"Valor total da compra R${self.__Total_Roupa}\n")
        return Str

    def __del__(self):
        print ("Roupa")

class Camisa(Roupa):

    __Cam_Tipo = None
    __Cam_Botoes = None
    __Cam_Bolso = None
    __Cam_Gola = None

    def __init__(self):
        super().__init__()
        self.__Cam_Tipo = " "
        self.__Cam_Botoes = 0
        self.__Cam_Bolso = 0
        self.__Cam_Gola = False
    
    def leitura(self):
        super().leitura()
        self.__Cam_Tipo = input("Digite o tipo da camisa:")
        self.__Cam_Botoes = int(input("Digite quantos botões tem:"))
        self.__Cam_Bolso = int(input("Quantos bolsos tem:"))
        a = input("Tem gola? S/N:")
        a.upper()
        if a == "S":
            self.__Cam_Gola = True
        else:
            self.__Cam_Gola = False
    
    def toString(self):
        
        Str = (super().toString() +
               f"Tipo da Camisa : {self.__Cam_Tipo}\n"
               f"Botões da camisa  : {self.__Cam_Botoes}\n"
               f"Bolso da camisa : {self.__Cam_Bolso}\n"
               f"Gola :{self.__Cam_Gola}\n")
        return Str

    def __del__(self):
        super().__del__()
        print ("Camisa")

a = Camisa()
a.leitura()
a.calcula_total()
print(a.toString())
del(a)

sys.exit(0)